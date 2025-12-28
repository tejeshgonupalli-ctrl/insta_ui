from utils.watermark_image import add_watermark_to_image

print("START TEST")

out = add_watermark_to_image(
    "posts/img1.jpg",
    "@test_watermark"
)

print("OUTPUT:", out)
