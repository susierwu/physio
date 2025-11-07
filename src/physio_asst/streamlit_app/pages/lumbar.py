from body_region_app import run_body_region_app

from region_configs.lumbar_config import (
    LUMBAR_SYSTEM_PROMPT,
    COMPARE_PROMPT,
    QA_SYSTEM_PROMPT,
    LUMBAR_REHAB_LINKS,
)


run_body_region_app(
    region_name="Lumbar (lower back)",
    system_prompt=LUMBAR_SYSTEM_PROMPT,
    compare_prompt=COMPARE_PROMPT,
    qa_prompt=QA_SYSTEM_PROMPT,
    rehab_links=LUMBAR_REHAB_LINKS, 
)
