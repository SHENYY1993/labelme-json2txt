import json
import os


def json_to_txt(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    label = data["shapes"][0]["label"]  # Assuming there's only one shape per JSON file
    shapes = data["shapes"]
    imagePath = data["imagePath"]
    imageWidth = data["imageWidth"]
    imageHeight = data["imageHeight"]

    txt_data = []
    for shape in shapes:
        points = shape["points"]

        x_center = 0.5 * (points[0][0] + points[1][0]) / imageWidth
        y_center = 0.5 * (points[0][1] + points[1][1]) / imageHeight
        w = (points[1][0] - points[0][0]) / imageWidth
        h = (points[1][1] - points[0][1]) / imageHeight
        txt_data.append(f"{label} {' '} {x_center} {' '}{y_center} {' '}{w} {' '}{h}")

    return " ".join(txt_data)


def convert_json_to_txt_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            json_file = os.path.join(folder_path, filename)
            txt_data = json_to_txt(json_file)
            with open(os.path.splitext(json_file)[0] + ".txt", 'w') as txt_file:
                txt_file.write(txt_data)


# 使用示例
folder_path = "C:/Users/shen_/Desktop/ULD_Dataset_20240511"
convert_json_to_txt_folder(folder_path)
