from PySide6.QtCore import QThread, Signal
from threadpoolctl import ThreadpoolController
import numpy as np
import amico
from os import path

class LoadDataWorker(QThread):
    complete_signal = Signal()
    error_signal = Signal(str)

    def __init__(
        self,
        model,
        study,
        subject,
        dwi,
        b0_threshold,
        mask=None,
        bvals=None,
        bvecs=None,
        b_step=None,
        delta=None,
        small_delta=None,
        te=None,
        schemefile=None
    ):
        super().__init__()
        self.model = model
        self.study = study
        self.subject = subject
        self.dwi = dwi
        self.b0_threshold = float(b0_threshold)
        self.mask = mask if mask else None
        self.bvals = bvals if bvals else None
        self.bvecs = bvecs if bvecs else None
        self.b_step = float(b_step) if b_step else None
        self.delta = float(delta) if delta else None
        self.small_delta = float(small_delta) if small_delta else None
        self.te = float(te) if te else None
        self.schemefile = schemefile if schemefile else None

    def run(self):
        self.evaluation = amico.Evaluation(self.study, self.subject)

        if not self.schemefile:
            schemefile = path.dirname(self.bvals)
            if self.model == 'NODDI':
                schemefile = path.join(schemefile, 'NODDI_scheme.scheme')
                try:
                    self.schemefile = amico.util.fsl2scheme(
                        bvalsFilename=self.bvals,
                        bvecsFilename=self.bvecs,
                        schemeFilename=schemefile,
                        bStep=self.b_step
                    )
                except:
                    self.error_signal.emit('Failed to create scheme file. See log for details.')
                    return
            if self.model == 'SANDI':
                schemefile = path.join(schemefile, 'SANDI_scheme.scheme')
                try:
                    self.schemefile = amico.util.sandi2scheme(
                        bvalsFilename=self.bvals,
                        bvecsFilename=self.bvecs,
                        Delta_data=self.delta,
                        smalldel_data=self.small_delta,
                        TE_data=self.te,
                        schemeFilename=schemefile,
                        bStep=self.b_step
                    )
                except:
                    self.error_signal.emit('Failed to create scheme file. See log for details.')
                    return
        
        if self.model == 'SANDI':
            self.evaluation.set_config('doDirectionalAverage', True) # TODO make parameter

        try:
            self.evaluation.load_data(dwi_filename=self.dwi, scheme_filename=self.schemefile, mask_filename=self.mask, b0_thr=self.b0_threshold)
        except:
            self.error_signal.emit('Failed to load data. See log for details.')
            return

        self.complete_signal.emit()

class SetupModelWorker(QThread):
    complete_signal = Signal()
    error_signal = Signal(str)

    def __init__(
        self,
        model,
        evaluation: amico.Evaluation,
        lmax,
        ndirs,
        openblas_num_threads,
        diff_par=None,
        diff_iso=None,
        ic_vf_lb=None,
        ic_vf_ub=None,
        ic_vf_n=None,
        ic_od_lb=None,
        ic_od_ub=None,
        ic_od_n=None, # TODO exvivo paramenter
        diff_is=None,
        radius_lb=None,
        radius_ub=None,
        radius_n=None,
        diff_in_lb=None,
        diff_in_ub=None,
        diff_in_n=None,
        diff_eciso_lb=None,
        diff_eciso_ub=None,
        diff_eciso_n=None,
    ):
        super().__init__()
        self.model = model
        self.evaluation = evaluation
        self.lmax = int(lmax)
        self.ndirs = int(ndirs) if model == 'NODDI' else 1 if model == 'SANDI' else int(ndirs)
        self.openblas_num_threads = int(openblas_num_threads)
        self.diff_par = float(diff_par) if diff_par else None
        self.diff_iso = float(diff_iso) if diff_iso else None
        self.ic_vf_lb = float(ic_vf_lb) if ic_vf_lb else None
        self.ic_vf_ub = float(ic_vf_ub) if ic_vf_ub else None
        self.ic_vf_n = int(ic_vf_n) if ic_vf_n else None
        self.ic_od_lb = float(ic_od_lb) if ic_od_lb else None
        self.ic_od_ub = float(ic_od_ub) if ic_od_ub else None
        self.ic_od_n = int(ic_od_n) if ic_od_n else None
        self.diff_is = float(diff_is) if diff_is else None
        self.radius_lb = float(radius_lb) if radius_lb else None
        self.radius_ub = float(radius_ub) if radius_ub else None
        self.radius_n = int(radius_n) if radius_n else None
        self.diff_in_lb = float(diff_in_lb) if diff_in_lb else None
        self.diff_in_ub = float(diff_in_ub) if diff_in_ub else None
        self.diff_in_n = int(diff_in_n) if diff_in_n else None
        self.diff_eciso_lb = float(diff_eciso_lb) if diff_eciso_lb else None
        self.diff_eciso_ub = float(diff_eciso_ub) if diff_eciso_ub else None
        self.diff_eciso_n = int(diff_eciso_n) if diff_eciso_n else None

    def run(self):
        try:
            amico.core.setup(lmax=self.lmax, ndirs=self.ndirs)
        except:
            self.error_signal.emit('Failed to generate auxiliary matrices. See log for details.')
            return

        self.evaluation.set_model(self.model)

        if self.evaluation.model.name == 'NODDI':
            self.evaluation.model.set(
                dPar=self.diff_par*1e-3,
                dIso=self.diff_iso*1e-3,
                IC_VFs=np.linspace(self.ic_vf_lb, self.ic_vf_ub, self.ic_vf_n),
                IC_ODs=np.hstack((np.array([0.03, 0.06]), np.linspace(self.ic_od_lb, self.ic_od_ub, self.ic_od_n))),
                isExvivo=False # TODO exvivo parameter
            )
        elif self.evaluation.model.name == 'SANDI':
            self.evaluation.model.set(
                d_is=self.diff_is*1e-3,
                Rs=np.linspace(self.radius_lb, self.radius_ub, self.radius_n)*1e-6,
                d_in=np.linspace(self.diff_in_lb, self.diff_in_ub, self.diff_in_n)*1e-3,
                d_isos=np.linspace(self.diff_eciso_lb, self.diff_eciso_ub, self.diff_eciso_n)*1e-3
            )
        
        controller = ThreadpoolController()

        try:
            with controller.limit(limits=self.openblas_num_threads, user_api='blas'):
                self.evaluation.generate_kernels(regenerate=True, lmax=self.lmax, ndirs=self.ndirs) # TODO regenenrate parameter
        except:
            self.error_signal.emit('Failed to generate kernels. See log for details.')
            return

        try:
            with controller.limit(limits=self.openblas_num_threads, user_api='blas'):
                self.evaluation.load_kernels()
        except:
            self.error_signal.emit('Failed to load kernels. See log for details.')
            return

        self.complete_signal.emit()

class FitModelWorker(QThread):
    complete_signal = Signal()
    error_signal = Signal(str)

    def __init__(
        self,
        evaluation: amico.Evaluation,
        joblib_backend,
        joblib_num_threads,
        lambda1,
        lambda2
    ):
        super().__init__()
        self.evaluation = evaluation
        self.joblib_backend = joblib_backend
        self.joblib_num_threads = int(joblib_num_threads)
        self.lambda1 = float(lambda1)
        self.lambda2 = float(lambda2)

        self.evaluation.set_config('parallel_backend', self.joblib_backend)
        self.evaluation.set_config('parallel_jobs', self.joblib_num_threads)

    def run(self):
        self.evaluation.set_solver(lambda1=self.lambda1, lambda2=self.lambda2)

        try:
            self.evaluation.fit()
        except:
            self.error_signal.emit('Failed to fit the model. See log for details.')
            return

        try:
            if self.evaluation.model.name == 'NODDI':
                self.evaluation.save_results()
            elif self.evaluation.model.name == 'SANDI':
                self.evaluation.save_results(save_dir_avg=True) # TODO save_dir_avg parameter
        except:
            self.error_signal.emit('Failed to save results. See log for details.')
            return

        self.complete_signal.emit()