import pytest
import imaging.lens_vignette_ca as mod

CASES = [
    ("vignette_table", (1,)),
    ("ca_channel_scale", (1,)),
    ("edge_reflect_pad", (1,)),
    ("exif_per_image", (1,)),
    ("float_pipeline", (1,)),
    ("determinism", (1,)),
    ("corner_luma_check", (1,)),
    ("validation", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("lens_profile", (1,)),
    ("metrics", (1,)),
    ("correct", (1,)),
    ("sample_channel", (1,)),
    ("output", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
