# cityscapes-dataset

## Getting Started
In order to use the Cityscapes dataset, you need to create an account on their website (https://www.cityscapes-dataset.com/). You must log in to download the data, which makes it difficult to download the data directly onto your server. You can use the script provided here to download the data directly.
<br /> 

To download the data, run the following command. Replace myusername and mypassword with your own credentials for the cityscapes website.  
```
python download_dataset.py --data-dir data/cityscapes --package-ids 1,3,7 --unzip --username myusername --password mypassword
```

Use the following mapping for the value of `package-ids`. This mapping can also be found on the [Cityscapes website](https://www.cityscapes-dataset.com/downloads/) by hovering over each download link.

1: gtFine_trainvaltest.zip (241MB) <br /> 
2: gtCoarse.zip (1.3GB) <br /> 
3: leftImg8bit_trainvaltest.zip (11GB) <br /> 
4: leftImg8bit_trainextra.zip (44GB) <br /> 
5: rightImg8bit_trainvaltest.zip <br /> 
6: rightImg8bit_trainextra.zip <br /> 
7: disparity_trainvaltest.zip (3.5GB) <br /> 
8: camera_trainvaltest.zip (2MB) <br /> 
9: camera_trainextra.zip (8MB) <br /> 
10: vehicle_trainvaltest.zip (2MB) <br /> 
11: vehicle_trainextra.zip (7MB) <br /> 
12: leftImg8bit_demoVideo.zip (6.6GB) <br /> 
13: all_demoVideo.zip <br /> 
14: leftImg8bit_sequence_trainvaltest.zip <br /> 
15: rightImg8bit_sequence_trainvaltest.zip <br /> 
16: leftImg16bit_trainvaltest.zip <br /> 
17: leftImg16bit_trainextra.zip <br /> 
18: ‘rightImg16bit_trainvaltest.zip <br /> 
19: rightImg16bit_trainextra.zip <br /> 
20: vehicle_sequence.zip <br /> 
21: timestamp_sequence.zip <br /> 
22: disparity_trainextra.zip (15GB) <br /> 
23: leftImg8bit_allFrames_frankfurt.zip <br /> 
24: timestamp_allFrames_frankfurt.zip <br /> 
25: vehicle_allFrames_frankfurt.zip <br /> 
26: disparity_sequence_trainvaltest.zip <br /> 
27: rightImg8bit_allFrames_frankfurt.zip <br /> 
28: gtBbox_cityPersons_trainval.zip <br /> 
29: leftImg8bit_trainvaltest_foggy.zip <br /> 
30: leftImg8bit_trainextra_foggy.zip <br /> 
31: leftImg8bit_trainval_foggyDBF.zip <br /> 
32: leftImg8bit_blurred.zip <br /> 
33: leftImg8bit_trainval_rain.zip <br /> 
34: gtBbox3d_trainvaltest.zip <br /> 
35: gtFinePanopticParts_trainval.zip <br /> 
