import os



dataset_name='ffhq' 
output_path='./npy/beard'

cmd0 = "python prepare_w.py"
### cmd1 = f"python GetCode.py --dataset_name {dataset_name} --output_path {output_path} --code_type 'w' --no_truncation"
cmd2 = f"python GetCode.py --dataset_name {dataset_name} --output_path {output_path} --code_type 's_flat' "
cmd3 = f"python GetCode.py --dataset_name {dataset_name} --output_path {output_path} --code_type 'images'  --resize 256 "

os.system(cmd0)
# # os.system(cmd1)
os.system(cmd2)
os.system(cmd3)


img_path=output_path+'/images.npy'
save_path=output_path+'/attribute'
classifer_path='./metrics_checkpoint/att'


cmd4 = f"python GetAttribute.py -img_path {img_path} -save_path {save_path} -classifer_path {classifer_path} "

os.system(cmd4)


cmd5 = f"python MAdvance.py "

os.system(cmd5)