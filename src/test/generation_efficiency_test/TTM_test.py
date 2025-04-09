
from TTMModule import TTMModule

my_module = TTMModule()

"""
Time cost for each term:
16.65, 9.96, 10.94, 15.38, 18.07 seconds.
"""
prompt_list = [
    "A boy is eating apple",
    "A boy is eating a green apple",
    "A handsome boy is eating a green apple",
    "A handsome boy is eating pizza with another girl",
    "A handsome boy is eating pizza with another girl, and he accidentally dropped it on the floor."
]

"""
Time cost for each term:
12.67, 12.45, 14.32, 18.02, 15.79

- The outcome for the first four images are very decent & continuous; quality of the last image is bad.
"""
long_prompt_list = [
    "Once upon a time there was a dear little girl who was loved by every one who looked at her, but most of all by her grandmother, and there was nothing that she would not have given to the child.",
    "Once she gave her a little cap of red velvet, which suited her so well that she would never wear anything else. So she was always called Little Red Riding Hood.",
    "One day her mother said to her, \"Come, Little Red Riding Hood, here is a piece of cake and a bottle of wine. Take them to your grandmother, she is ill and weak, and they will do her good. \"",
    "Little Red Riding Hood raised her eyes, and when she saw the sunbeams dancing here and there through the trees, and pretty flowers growing everywhere, she thought, suppose I take grandmother a fresh nosegay. That would please her too. It is so early in the day that I shall still get there in good time.",
    "And scarcely had the wolf said this, than with one bound he was out of bed and swallowed up Little Red Riding Hood."
]


# for i in range(len(long_prompt_list)):
for i in [2]:
    print(f"It takes {round(my_module.generate_image(prompt_list[i]), 2)} seconds to generate image {i+1}");