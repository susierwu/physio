# src/physio_asst/streamlit_app/region_configs/shoulder_config.py

SHOULDER_SYSTEM_PROMPT = """
You are an expert physiotherapist AI. You will receive a text description of a shoulder radiology (e.g., x-ray, MRI, ultrasound) results.
From the text, identify the three most likely shoulder conditions from this list:

Shoulder Impingement, Degenerative Rotator Cuff Tear, Calcific Tendinopathy, Thoracic Outlet Syndrome,
Acute Torticollis, Benign Joint Hypermobility Syndrome, Clavicle Fracture,
Acromioclavicular Joint Injury, Shoulder Osteoarthritis (OA), Shoulder Dislocation,
Whiplash Disorders, Frozen Shoulder, Rotator Cuff Tendinopathy, Biceps Tendinopathy

Read the radiology description carefully and identify the three most likely conditions.
Return your answer in this format:
    1.  Name – Confidence 
    2.  Name – Confidence 
    3.  Name – Confidence
A new line for each condition. Briefly justify why these are likely based on the radiology findings.
If user input is bilingual (e.g., partly in Chinese), respond in the same language mix naturally.
"""



SHOULDER_REHAB_LINKS = {
    "Shoulder Impingement": "https://purephysiotherapy.co.uk/exercise-plans/early-shoulder-impingement-exercise-programme/",
    "Degenerative Rotator Cuff Tear": "https://purephysiotherapy.co.uk/exercise-plans/early-degenerative-rotator-cuff-tear-exercise-programme/",
    "Calcific Tendinopathy": "https://purephysiotherapy.co.uk/exercise-plans/early-calcific-tendinopathy-exercise-programme/",
    "Thoracic Outlet Syndrome": "https://purephysiotherapy.co.uk/exercise-plans/early-thoracic-outlet-syndrome-exercise-programme/",
    "Acute Torticollis": "https://purephysiotherapy.co.uk/exercise-plans/early-acute-torticollis-exercise-programme/",
    "Benign Joint Hypermobility Syndrome": "https://purephysiotherapy.co.uk/exercise-plans/early-benign-joint-hypermobility-syndrome-exercise-programme/",
    "Clavicle Fracture": "https://purephysiotherapy.co.uk/exercise-plans/early-clavicle-fracture-exercise-programme/",
    "Acromioclavicular Joint Injury": "https://purephysiotherapy.co.uk/exercise-plans/early-acromioclavicular-joint-injury-exercise-programme/",
    "Shoulder Osteoarthritis (OA)": "https://purephysiotherapy.co.uk/exercise-plans/early-shoulder-osteoarthritis-exercise-programme/",
    "Shoulder Dislocation": "https://purephysiotherapy.co.uk/exercise-plans/early-shoulder-dislocation-exercise-programme/",
    "Whiplash Disorders": "https://purephysiotherapy.co.uk/exercise-plans/early-whiplash-disorders-exercise-programme/",
    "Frozen Shoulder": "https://purephysiotherapy.co.uk/exercise-plans/early-frozen-shoulder-exercise-programme/",
    "Rotator Cuff Tendinopathy": "https://purephysiotherapy.co.uk/exercise-plans/early-rotator-cuff-tendinopathy-exercise-programme/",
    "Biceps Tendinopathy": "https://purephysiotherapy.co.uk/exercise-plans/early-biceps-tendinopathy-exercise-programme/"
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



SHOULDER_INFO_LINK = "https://purephysiotherapy.co.uk/understanding-shoulder-pain-causes-risks-and-physiotherapy-treatments/"

SHOULDER_CONDITIONS = [
    "Shoulder Impingement – 肩部撞击综合征",
    "Degenerative Rotator Cuff Tear – 退行性肩袖撕裂",
    "Calcific Tendinopathy – 钙化性肌腱病",
    "Thoracic Outlet Syndrome – 胸廓出口综合征",
    "Acute Torticollis – 急性斜颈",
    "Benign Joint Hypermobility Syndrome – 良性关节过度活动综合征",
    "Clavicle Fracture – 锁骨骨折",
    "Acromioclavicular Joint Injury – 肩锁关节损伤",
    "Shoulder Osteoarthritis (OA) – 肩关节骨关节炎",
    "Shoulder Dislocation – 肩关节脱位",
    "Whiplash Disorders – 甩鞭伤综合征",
    "Frozen Shoulder – 冻结肩 / 肩周炎",
    "Rotator Cuff Tendinopathy – 肩袖肌腱病变",
    "Biceps Tendinopathy – 肱二头肌肌腱病变",
]
 