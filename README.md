# AR Structural Biology Viewer

This project provides a **free** web-based AR viewer for 3D models for teaching structural biology, optimized for both iOS and Android devices. Students can scan QR codes to view different biological structures in augmented reality or 3D without any specific app.

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

If you take nice AR picture please share !!

If you found this project useful, used it, or needed to customize it, please let me know! 
Your feedback is essential to help me improve and continue this project. You can reach out to me directly at reach out to me via email.

## Features

- **Cross-Platform Support**: Automatically detects the user's device (iOS or Android) and loads the appropriate 3D model format (USDZ for iOS, GLB for Android).
- **Augmented Reality**: Allows users to view 3D models in AR if their device supports it.
- **Dynamic Model Loading**: QR codes link to specific models, which are dynamically loaded based on the URL parameters.
- **Python script to generate free QR code**: You can easily generate the different QR code to link URL to specific models.
- **Pymol, Chimera and Blender** are use to genrate 3D models.
- Even Faster you can use **Mol'*'** (https://molstar.org/viewer/) that can directly export your model in usdz and glb format, ready to be uploaded on your server.
- You can also have look to **MolAR** (https://mtzgroup.github.io/molar/).

## Usage

### Viewing Models
1. **Use a link with smartphone or tablet etc...**
      For example you can have access to the 20 amino acids (model15 to model34)
      by with the following link:

      https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=modelXX
     
     just change the model number XX for the coresponding aa:
     
 ALA:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model15 

ARG:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model16 

ASN:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model17 

ASP:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model18 

CYS:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model19 

GLN:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model20 

GLU:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model21 

GLY:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model22 

HIS:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model23 

ILE:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model24 

LEU:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model25 

LYS:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model26 

MET:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model27 

PHE:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model28 

PRO:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model29 

SER:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model30 

THR:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model31 

TRP:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model32 

TYR:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model33 

VAL:
 https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model34 

  
## QR Codes

2. **Use a a QR Code**
You can also use a QR code scanner on your mobile device to scan the QR code associated with the desired model (for presentation, poster etc ...).
   (for ipad make sure that safari is in mobile version)

Here are some QR codes for some models:

### Alpha Helix
<img src="QR-Code/a-helix.png" alt="Alpha Helix" width="150" height="150">

### Beta Sheet
<img src="QR-Code/beta-sheet.png" alt="Beta Sheet" width="150" height="150">

### DNA
<img src="QR-Code/DNA.png" alt="DNA" width="150" height="150">

### mCherry
<img src="QR-Code/mcherry.png" alt="mCherry" width="150" height="150">

### Haemoglobin
<img src="QR-Code/hemo.png" alt="Haemoglobin" width="150" height="150">

**Open the Link**: The link will direct you to the web viewer, which will automatically detect your device and load the appropriate model depending of iOS or Android.

**Click on the cube at the bottom right**
<img src="Divers/ar-icon.png" alt="Cube" width="100" height="100">

**See the magic, your model in your world**
<img src="Divers/DNA.jpg" alt="AR-DNA" width="150" height="250">

**Display just the 3D model without AR**

  You have the possibility to just display the model in 3D by clicking on 'object' (for iOS), 3D (for Android)

<img src="Divers/1lmb.png" alt="AR-DNA" width="150" height="250">

3. **Just have Fun**
   
  Today's fluorescent assay is glowing in a vibrant …
  
… **mcherry**!


https://github.com/user-attachments/assets/bfa177a1-5bc0-483a-8956-927bb8eb15a4

4. **another way to learn**


https://github.com/user-attachments/assets/8d391bb7-de8d-4201-99d2-7d9b1601902c



## Generating 3D Models for AR Viewer

To create and optimize 3D models for the AR viewer, follow this pipeline using PyMOL, Chimera, Blender, and MeshLab:

1. **Create Your Model in PyMOL or Chimera:**
   - Design your 3D molecular structure or other models using PyMOL or Chimera.
   - Export the model in the VRML 2 format.
   - if you use **Mol'*'** (https://molstar.org/viewer/) you can direclty export the model in usdz or glb.

2. **Import and Process in Blender:**
   - **Importing the Model:**
     - Open Blender and /!\ enable the `Web3D X3D/VRML2` add-on /!\ , which allows for importing VRML 2 files.
     - Import the VRML 2 model into Blender.
   - **Processing in Blender:**
     - Refine the model, adjust textures, and prepare it for AR use. Ensure the model's scale and orientation are appropriate.
   - **Exporting to USDZ and GLB:**
     - Export the model in both USDZ (for iOS) and GLB (for Android) formats, ensuring cross-platform compatibility.

3. **Optimizing Large Models with MeshLab:**
   - **keeping the color** (thx to @Allister_crow)
    - Open the VRML 2 model in Meslab
    - under color Creation and Processing -> transfert color to vertex to face 
    - under color Creation and Processing -> tranfert color face to vertex 
    - save the model to *.obj and then go to blender (step2)

   - **Handling Large Structures:**
     - For complex models resulting in large file sizes, use MeshLab to optimize the model using cleanning tools.
   - **Decimation and Cleaning:**
     - Utilize MeshLab's decimation tools to reduce polygon count and make the model more efficient for AR applications.
   - **Final Export:**
     - After optimization, re-export the model in VRML to import with blender to then export in USDZ and GLB formats 

By following this pipeline, you can produce high-quality, optimized 3D models that enhance the AR experience for users.

### Load models on github
   
   ### 1- Add on github your 3D models in the IOS directory (.usdz) and in the Android directory (.glb)
   
   ### 2- Edit the file: `models.json` 
    Update `models.json` with the appropriate URLs for your 3D model files.
    "modelXX": { "ios": "YY.usdz", "android": "YY.glb" }
    ```json
    {
        "model1": { "ios": "a-helix.usdz", "android": "a-helix.glb" },
        "model2": { "ios": "beta-sheet.usdz", "android": "beta-sheet.glb" },
        ...
    }
    ```
   ### 3- Generating QR Codes

Generate QR codes that link to your hosted `models.json` with the appropriate model query parameter.
 For example:
- **Alpha Helix**: `https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model1`
- **Beta Sheet**: `https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model2`
- **DNA**: `https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model3`
- **mCherry**: `https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model4`
- **B-galactosidase**: `https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model5`
- **Haemoglobin**: `https://jmb-scripts.github.io/AR-Structural-Biology/index.html?model=model6`

   You can use a QR code generator Qr-code.py in QR-Code/:

  1. **Edit Qr-code.py**
        change the URL line 25 with the proper model number

  2. **Then in a terminal type:**

     `python Qr-code.py`

  4. **Share the PNG** on your website, in your scientific poster, or presentation etc...

  ### 4- The index.html will then depending of the mobile OS redirect to the correct model.
  
## Thx
- To @Allister_crow for its walkthrough on the use of AR for structural biology.
- To chatgpt because HTML is not my friend.
