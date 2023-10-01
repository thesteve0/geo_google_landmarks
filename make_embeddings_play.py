import numpy as np
import torch
from thingsvision import get_extractor
from thingsvision.utils.storing import save_features
from thingsvision.utils.data import ImageDataset, DataLoader

source = 'custom'
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model_name = 'clip'
model_parameters = {
    'variant': 'ViT-B/32'
    # This model creates 512 length vectors
}

# This model is more accurate but takes longer to run and not sure we need it for the demo
# model_name = 'OpenCLIP'
# model_parameters = {
#     'variant': 'ViT-H-14',
#     'dataset': 'laion2b_s32b_b79k'
#     # This model create 1024 length vectors
# }

extractor = get_extractor(
    model_name=model_name,
    source=source,
    device=device,
    pretrained=True,
    model_parameters=model_parameters,
)

root='../test_images/' # (e.g., './images/)
batch_size = 32

dataset = ImageDataset(
    root=root,
    out_path='../test_vectors',
    backend=extractor.get_backend(), # backend framework of model
    transforms=extractor.get_transformations(resize_dim=256, crop_dim=224) # set the input dimensionality to whichever values are required for your pretrained model
)

batches = DataLoader(
    dataset=dataset,
    batch_size=batch_size,
    backend=extractor.get_backend() # backend framework of model
)


module_name = 'visual'

def get_features():
    # we are creating 1024 length vectors
    features = extractor.extract_features(
        batches=batches,
        module_name=module_name,
        flatten_acts=True,
        output_type="ndarray", # or "tensor" (only applicable to PyTorch models of which CLIP is one!)
    )

    # WE ARE NOT DOING THIS append the file names to the front of the vector matrix.  We turn the file names into a 40 x 1
    # np array #full_data = np.hstack((np.array(dataset.file_names).reshape(-1,1), features))
    # The model returns the vectors in alphbetical order for the filenames. Our other code just reads through the directory
    # without a sort.  Therefore this needs to be a dict so we can do lookups

    # save_features(features, out_path='../test_vectors', file_format='txt') # file_format can be set to "npy", "txt", "mat", "pt", or "hdf5"

    vectors = {}
    for i in range(len(dataset.file_names)):
        vectors[dataset.file_names[i][0:16]] = features[i]

    return vectors


if __name__ == '__main__':
    result = get_features()
    print(str(len(result)))

