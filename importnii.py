import vtk

pathgm = r'E:\Imaging\spine generic\sub-amu02processed\sub-amu02_T2star_gmseg.nii.gz'

import vtk

# Load the NIFTI image file using vtkNIFTIImageReader
reader = vtk.vtkNIFTIImageReader()
reader.SetFileName(pathgm)
reader.Update()

# Create a rendering window, renderer, and interactor
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Create a mapper
mapper = vtk.vtkFixedPointVolumeRayCastMapper()
mapper.SetInputData(reader.GetOutput())

# Create a volume
volume = vtk.vtkVolume()
volume.SetMapper(mapper)

# Add the volume to the renderer
ren.AddVolume(volume)

# Set the camera position and render the scene
ren.ResetCamera()
renWin.Render()

# Start the interactor
iren.Start()





# def load_data_3d(self, img_3d):
#      rdr = vtk.vtkNIFTIImageReader()
#      rdr.SetFileName(img_3d)
#      rdr.Update()
#      rdr.GetOutput()
#      self.rdr=rdr
#      print(rdr.GetOutput())
#      outline_actor = self.create_outline()
#      self.renderer.AddActor(outline_actor)
#      self.widget()
#      self.renderer.ResetCamera()
#      self.render_window.Render()


#       def change_dialog_3D(self, load_3d):
#      rdr = vtk.vtkNIFTIImageReader()
#      rdr.SetFileName(load_3d)
#      rdr.Update()
#      self.img.SetInputData(rdr.GetOutput())
#      self.outline.SetInputData(rdr.GetOutput())
#      self.render_window.Render()
#      self.rdr = rdr