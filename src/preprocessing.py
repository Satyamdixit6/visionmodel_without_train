import torch 
import torchvision.transforms.v2 as v2
import os




def preprocessing(file_path:str)->torch.Tensor:
   image_dir = file_path
    
   images=os.listdir(image_dir)

    #tranform=v2.Compose([v2.Resize([512,512],interpolation=)])
   list_imgae=[]
   for img in images:
      img
      list_imgae.append(img)
   return list_imgae
   
       
        
test=preprocessing("C:/Users/satya/OneDrive/Desktop/model_file_tune/dog")
print(test[1])

