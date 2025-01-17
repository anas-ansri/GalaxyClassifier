import numpy as np
import pandas as pd
import yaml


def labels():
    with open(config()["directories"]["labels"], "r") as file:
        df = pd.read_csv(file)
    return df


def config():
    with open("config.yml", "r") as file:
        contents = yaml.safe_load(file)
    return contents


def reference_table():
    ref_table_dir = config()["directories"]["ref_table"]
    ref_table = pd.read_csv(ref_table_dir)
    obj_id = np.array(ref_table["objid"])
    sample = np.array(ref_table["sample"])
    img_id = np.array(ref_table["asset_id"])
    return pd.DataFrame(np.array((sample, img_id)).T, columns=["SAMPLE", "IMG_ID"], index=obj_id)


def gz2_table2():
    gz_table_dir = config()["directories"]["gal_zoo2_table2"]
    gz_table = pd.read_csv(gz_table_dir)
    obj_id = gz_table["OBJID"]
    spiral = gz_table["SPIRAL"]
    elliptical = gz_table["ELLIPTICAL"]
    dk = gz_table["UNCERTAIN"]
    return pd.DataFrame(
        np.array((spiral, elliptical, dk)).T,
        columns=["SPIRAL", "ELLIPTICAL", "UNCERTAIN"],
        index=obj_id
    )


def gz2_metadata_table():
    meta_table_dir = config()["directories"]["gal_zoo2_metadata_table"]
    metadata = pd.read_csv(meta_table_dir)
    for col in metadata.columns:
        print(col)
    object_id = metadata["OBJID"]
    eg = metadata["EXTINCTION_G"]
    er = metadata["EXTINCTION_R"]
    extinction = eg - er
    extinction.index = object_id
    return pd.DataFrame(extinction)
