# from ultralytics import YOLO

# model = YOLO('/home/tanmoy/Computer Vision Project/Football player Analysis project/models/best.pt')

# results = model.predict('input_videos/08fd33_4.mp4',save =True)
# print(results[0])
# print('==================================')
# for box in results[0].boxes:
#     print(box)
    

from ultralytics import YOLO

# Load the model
try:
    model = YOLO('/home/tanmoy/Computer Vision Project/Football player Analysis project/models/best.pt')
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Run the prediction
try:
    results = model.predict('input_videos/08fd33_4.mp4', save=True, save_dir='/home/tanmoy/Computer Vision Project/Football player Analysis project/runs/predict', verbose=True)
except Exception as e:
    print(f"Error running prediction: {e}")
    exit()

# Print the results
print(results[0])
print('==================================')
for box in results[0].boxes:
    print(box)


