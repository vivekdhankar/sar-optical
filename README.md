# sar-optical
Synthetic aperture radar (SAR) remote sensing plays an important role in Earth observation. The ability to interpret the data is limited, even for experts, as the human eye is not familiar with the impact of distance-dependent imaging, signal intensities detected in the radar spectrum as well as image characteristics related to speckles.
Optical remote sensing data suffer from the limitation of bad weather and cloud contamination, whereas synthetic aperture radar (SAR) can work under all weather
conditions and overcome this disadvantage of optical data. Therefore, the need for SAR-to-optical image-to-image translation becomes evident.

<h3>The challenge:</h3>

Our task is to train a Deep learning model, so that given a SAR image as input, the model should be able to output the translated optical image. It is an unpaired image-to-image translation problem.
Our model will be evaluated with objective image quality assessments: 

a) Peak signal-to-noise ratio (PSNR)

b) Structural similarity index (SSIM)


Dataset description and Links:
https://www.intelligence-airbusds.com/imagery/sample-imagery/
