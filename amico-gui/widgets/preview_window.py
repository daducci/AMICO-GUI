from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from preview_window_ui import Ui_window
from ui.preview_window_ui import Ui_window
from os import path, listdir
import nibabel as nib
import numpy as np

class PreviewWindow(QMainWindow):
    def __init__(self, preview_path):
        super().__init__()
        self.ui = Ui_window()
        self.ui.setupUi(self)

        self.preview_path = preview_path

        self.init_image_preview()
        self.load_slots()

    def init_image_preview(self):
        self.ui.graphicsView.show()
        self.images = [file for file in listdir(self.preview_path) if file.endswith('.nii.gz')]
        self.ui.comboBoxImagePreview.addItems(self.images)
        self.switch_image()

    def load_slots(self):
        self.ui.pushButtonView1.clicked.connect(lambda: self.switch_view('sagittal'))
        self.ui.pushButtonView2.clicked.connect(lambda: self.switch_view('coronal'))
        self.ui.pushButtonView3.clicked.connect(lambda: self.switch_view('axial'))
        self.ui.horizontalSlider.valueChanged.connect(self.update_slice)
        self.ui.comboBoxImagePreview.currentIndexChanged.connect(self.switch_image)

    @Slot()
    def switch_image(self):
        if self.ui.comboBoxImagePreview.currentText() != '':
            img = nib.load(path.join(self.preview_path, self.ui.comboBoxImagePreview.currentText()))
            img_data = img.get_fdata()
            
            self.sagittal_coronal = np.flip(img_data, axis=1)
            self.sagittal_coronal = np.flip(self.sagittal_coronal, axis=2)
            self.axial = np.flip(img_data, axis=1)

            self.view = 'axial'
            slice = self.axial.shape[2] // 2
            self.ui.horizontalSlider.setMinimum(0)
            self.ui.horizontalSlider.setMaximum(self.axial.shape[2]-1)
            self.ui.horizontalSlider.setValue(slice)
            self.ui.graphicsView.setImage(self.axial[:, :, slice])

    @Slot()
    def switch_view(self, view):
        if view == 'sagittal' and self.view != 'sagittal':
            self.view = 'sagittal'
            slice = self.sagittal_coronal.shape[0] // 2
            self.ui.horizontalSlider.setMaximum(self.sagittal_coronal.shape[0]-1)
            self.ui.horizontalSlider.setValue(slice)
            self.ui.graphicsView.setImage(self.sagittal_coronal[slice, :, :])
        elif view == 'coronal' and self.view != 'coronal':
            self.view = 'coronal'
            slice = self.sagittal_coronal.shape[1] // 2
            self.ui.horizontalSlider.setMaximum(self.sagittal_coronal.shape[1]-1)
            self.ui.horizontalSlider.setValue(slice)
            self.ui.graphicsView.setImage(self.sagittal_coronal[:, slice, :])
        elif view == 'axial' and self.view != 'axial':
            self.view = 'axial'
            slice = self.axial.shape[2] // 2
            self.ui.horizontalSlider.setMaximum(self.axial.shape[2]-1)
            self.ui.horizontalSlider.setValue(slice)
            self.ui.graphicsView.setImage(self.axial[:, :, slice])
            
    @Slot()
    def update_slice(self):
        slice = self.ui.horizontalSlider.value()
        if self.view == 'sagittal':
            self.ui.graphicsView.setImage(self.sagittal_coronal[slice, :, :])
        elif self.view == 'coronal':
            self.ui.graphicsView.setImage(self.sagittal_coronal[:, slice, :])
        elif self.view == 'axial':
            self.ui.graphicsView.setImage(self.axial[:, :, slice])