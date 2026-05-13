from body_region_app import run_body_region_app

from region_configs.shoulder_config import (
    SHOULDER_SYSTEM_PROMPT,
    COMPARE_PROMPT,
    QA_SYSTEM_PROMPT,
    SHOULDER_REHAB_LINKS,
)


SHOULDER_PREFILLED_EXAMPLE = """Clinical History: Right shoulder tendinitis post fall during ski in the winter. Exacerbation after physical activity

Comparison: Radiograph from the same day

Findings:

The long head of biceps tendon is intact and normally positioned in the bicipital groove.

The subscapularis tendon is intact.

The supraspinatus and infraspinatus tendons are intact. No sign of significant tendinosis. No high-grade or full-thickness tear.

There is no muscle atrophy in the supraspinatus or infraspinatus.

There is no thickening or fluid content in the subacromial subdeltoid bursa.

Unremarkable acromioclavicular joint on ultrasound.

There is overall decreased range of motion. Mild subacromial impingement on shoulder abduction.

Impression:

No high-grade or full-thickness rotator cuff tear or sign of tendinosis.

Overall decreased range of motion could indicate underlying adhesive capsulitis. Correlate clinically. If necessary, if there is no improvement of symptoms with conservative management, a fluoroscopic guided cortisone joint injection and distensive arthrography could be performed.
"""


run_body_region_app(
    region_name="Shoulder",
    system_prompt=SHOULDER_SYSTEM_PROMPT,
    compare_prompt=COMPARE_PROMPT,
    qa_prompt=QA_SYSTEM_PROMPT,
    rehab_links=SHOULDER_REHAB_LINKS, 
    prefilled_example=SHOULDER_PREFILLED_EXAMPLE,
)

