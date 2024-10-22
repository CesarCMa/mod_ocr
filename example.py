from easyocr import Reader

# print("Testing default params")
# reader = Reader(["ch_sim", "en"])  # this needs to run only once to load the model into memory
# result = reader.readtext("examples/chinese.jpg")
# print(result)

print("Testing zh_tra_g1 recog network")
reader = Reader(["ch_sim", "af"])  # this needs to run only once to load the model into memory
result = reader.readtext("examples/chinese.jpg")
print(result)

# print("Testing dbnet18") # DBNet takes too much to compile and fills all RAM of the system
# reader = Reader(
#     ["ch_sim", "en"], detect_network="dbnet18"
# )  # this needs to run only once to load the model into memory
# result = reader.readtext("examples/chinese.jpg")
# print(result)
