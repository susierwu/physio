# src/physio_asst/streamlit_app/region_configs/lumbar_config.py

LUMBAR_SYSTEM_PROMPT = """
You are an expert physiotherapist AI. You will receive a text description of a lower-back (lumbar spine) radiology (e.g., x-ray, MRI, ultrasound) results.
From the text, identify the three most likely lumbar conditions from this list:

Coccydynia
Lumbar Spine Osteoarthritis (OA)
Mechanical Back Pain
Lumbar Disc Injury
Spondylolysis
Sacroiliac Joint Dysfunction
Femoral Nerve Radiculopathy
Ankylosing Spondylitis
Spondylolisthesis
Benign Joint Hypermobility Syndrome
Cauda Equina Syndrome
Lumbar Spinal Stenosis
Deep Gluteal/Piriformis Syndrome
Low Back Pain and Sciatica
Greater Trochanteric Pain Syndrome
Femoroacetabular Impingement

 
Read the radiology description carefully and identify the three most likely conditions.
Return your answer in this format:
    1.  Name – Confidence 
    2.  Name – Confidence 
    3.  Name – Confidence
A new line for each condition. Briefly justify why these are likely based on the radiology findings.
If user input is bilingual (e.g., partly in Chinese), respond in the same language mix naturally.
"""



LUMBAR_REHAB_LINKS = {
    "Coccydynia": "https://purephysiotherapy.co.uk/exercise-plans/early-coccydynia-exercise-programme/", 
    "Lumbar Spine Osteoarthritis (OA)": "https://purephysiotherapy.co.uk/conditions/lumbar-spine-osteoarthritis-oa/", 
    "Mechanical Back Pain": "https://purephysiotherapy.co.uk/exercise-plans/early-mechanical-back-pain-exercise-programme/",  
    "Lumbar Disc Injury": "https://purephysiotherapy.co.uk/exercise-plans/early-lumbar-disc-injury-exercise-programme/", 
    "Spondylolysis": "https://purephysiotherapy.co.uk/exercise-plans/early-spondylolysis-exercise-programme/",   
    "Sacroiliac Joint Dysfunction": "https://purephysiotherapy.co.uk/exercise-plans/early-sacroiliac-joint-dysfunction-exercise-programme/",  
    "Femoral Nerve Radiculopathy": "https://purephysiotherapy.co.uk/exercise-plans/early-femoral-nerve-radiculopathy-exercise-programme/",   
    "Ankylosing Spondylitis": "https://purephysiotherapy.co.uk/exercise-plans/early-ankylosing-spondylitis-exercise-programme/",
    "Spondylolisthesis": "https://purephysiotherapy.co.uk/exercise-plans/early-spondylolisthesis-exercise-programme/", 
    "Benign Joint Hypermobility Syndrome": "https://purephysiotherapy.co.uk/exercise-plans/early-benign-joint-hypermobility-syndrome-exercise-programme/", 
    "Cauda Equina Syndrome": "https://purephysiotherapy.co.uk/exercise-plans/early-cauda-equina-syndrome-exercise-programme/",
    "Lumbar Spinal Stenosis": "https://purephysiotherapy.co.uk/exercise-plans/early-lumbar-spinal-stenosis-exercise-programme/",
    "Deep Gluteal/Piriformis Syndrome":  "https://purephysiotherapy.co.uk/exercise-plans/early-Deep-Gluteal-Piriformis Syndrome-exercise-programme/",
    "Low Back Pain and Sciatica": "https://purephysiotherapy.co.uk/exercise-plans/early-low-back-pain-and-sciatica-exercise-programme/", 
    "Greater Trochanteric Pain Syndrome":  "https://purephysiotherapy.co.uk/exercise-plans/Greater-Trochanteric-Pain-Syndrome-exercise-programme/",
    "Femoroacetabular Impingement":  "https://purephysiotherapy.co.uk/exercise-plans/early-Femoroacetabular-Impingement-exercise-programme/",
}





COMPARE_PROMPT = """
You are a physiotherapy decision-support AI.  You already reviewed the radiology and diagnosis.

radiology Findings:
{mri}

Diagnosis Summary:
{diagnosis}

Previous Dialogue:
{history}

Use the radiology findings and diagnosis to evaluate the two differing doctors opinions. For each doctor's advice, explain whether it is reasonable, why, and which approach is more appropriate. 
Make your explaination concise and understandable (not too much medical terms) to the user. 
If user input is in Chinese, respond in the same language, otherwise, use English.              
"""

           


QA_SYSTEM_PROMPT = """
You are a certified physiotherapist AI assistant. You already reviewed the radiology and diagnosis.

radiology Findings:
{mri}

Diagnosis Summary:
{diagnosis}

Previous Dialogue:
{history}

Now, you will receive the user's follow-up questions about anything (e.g., exercises, pain, rehab).
        Your tasks:
        1. Give a short, direct, evidence-based initial answer for each question (maximum 3 sentences).
        2. Provide medically conservative and safe guidance — 
           do NOT suggest any invasive procedure, unverified supplement, or unprescribed medication.
        3. If user input is bilingual (e.g., partly in Chinese), respond in the same language mix naturally.

DO NOT say in your answer, e.g.,  consult a physiotherapist, just give user your best avaialble answer.  
Be empathetic, precise, not too concise explain better in patient's langulage. and always within physiotherapy and rehabilitation boundaries.
"""



LUMBAR_INFO_LINK =  "https://purephysiotherapy.co.uk/understanding-lower-back-pain-and-sciatica-causes-risks-and-physiotherapy-treatments/"


LUMBAR_CONDITIONS = [
    "Coccydynia — 尾骨痛",
    "Lumbar Spine Osteoarthritis (OA) — 腰椎骨关节炎",
    "Mechanical Back Pain — 机械性背痛",
    "Lumbar Disc Injury — 腰椎间盘损伤",
    "Spondylolysis — 椎弓峡部裂",
    "Sacroiliac Joint Dysfunction — 骶髂关节功能障碍",
    "Femoral Nerve Radiculopathy — 股神经根病变",
    "Ankylosing Spondylitis — 强直性脊柱炎",
    "Spondylolisthesis — 椎体滑脱",
    "Benign Joint Hypermobility Syndrome — 良性关节过度活动综合征",
    "Cauda Equina Syndrome — 马尾综合征",
    "Lumbar Spinal Stenosis — 腰椎管狭窄症",
    "Deep Gluteal/Piriformis Syndrome — 深臀肌/梨状肌综合征",
    "Low Back Pain and Sciatica — 腰痛及坐骨神经痛",
    "Greater Trochanteric Pain Syndrome — 股骨大转子疼痛综合征",
    "Femoroacetabular Impingement — 髋臼撞击综合征"
]
 