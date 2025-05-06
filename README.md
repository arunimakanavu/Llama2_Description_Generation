# Category Description Generation Using Ollama- llama 2

## **Objective**
To efficiently generate professional and concise descriptions for **1033 L3 categories**, leveraging **LLaMA2 via Ollama API** for automation and applying manual refinement to ensure quality.

---

## **Workflow Overview**

| Step | Description | Time Estimate |
|------|-------------|----------------|
| 1 | Automated generation using LLaMA2 | ~5 hours |
| 2 | Manual review & refinement | ~6–8 hours |
| 3 | Final compilation & validation | ~1 hour |
| **Total** | **Complete process** | **~12–14 hours** |

---

## **Step 1: Automated Description Generation**

### 1.1. **Model and Script Details**
- **Model**: LLaMA2 (via Ollama API)
- **Input**: CSV file with `L2` and `L3` columns
- **Output**: CSV with generated `Description` column
- **Rate Limiting**: `1 second` delay between API calls
- **Function Enhancement**: Accepts both `L2` and `L3` for better context alignment

### 1.2. **Script Functionality**
````markdown
```python
def generate_description(l2, l3):
    prompt = f"Generate a professional, industry-specific description for the subcategory: {l3}, refering to the maincategory {l2}. The description should be concise (2 lines max, under 200 characters) and easy to understand."
    
    response = ollama.chat(model='llama2', messages=[{"role": "user", "content": prompt}])
    return response['message']['content']
```
````

### 1.3. **Execution Plan**
- **Batch Size**: 200–250 categories to prevent overload or timeout
- **Storage**: Save intermediate outputs in CSVs
- **Estimated Time**:  
  - 100 L3s: ~50 minutes  
  - Total 1033 L3s: ~8 hours (adjusted for new function and delays)

---

## **Step 2: Manual Review & Refinement**

### 2.1. **Accuracy Observations**
- **Auto-generated accuracy**: ~60–70%
- **Manual edits required**: 30–40% (approx. 310–415 categories)

### 2.2. **Time Estimate**
| Categories | Time (avg 45s/cat) | Hours |
|------------|---------------------|--------|
| 310 | ~3.9 hours |
| 415 | ~5.2 hours |
| **+ Buffer** | for deeper edits & team review | **~6–8 hours total** |

### 2.3. **Review Guidelines**
- Flag low-confidence descriptions
- Use a checklist:
  - ✅ Relevance to industry/domain
  - ✅ Brevity and clarity (≤ 2 lines, ≤ 200 characters)
  - ✅ No jargon or fluff
- **Team Review**: Distribute effort among 2–3 people if needed

---

## **Step 3: Final Compilation & Quality Check**

### 3.1. **Final QC Tasks**
- Ensure formatting consistency (tone, length, structure)
- Run spell-check and grammar review
- Verify no missing descriptions
- Compile and finalize master CSV

### 3.2. **Estimated Time**: ~1 hour

---

## **Risk Management Plan**

| Risk | Mitigation |
|------|------------|
| **API Rate Limits or Failures** | Run smaller batches (200–250) + retry logic |
| **High Manual Load** | Team-based review distribution |
| **Output Inconsistency** | Use review checklist + final QC round |
| **Script Errors** | Save intermediate batches regularly |

---

## **Sample Output Reference**
See: **Desc Set 1** (example descriptions for batch-6)

---

## **Conclusion**
Using a blend of **automated LLM-powered generation** and **human-led refinement**, this plan ensures high-quality L3 category descriptions can be completed within **2 working days** (~12–14 hours total). Contextual accuracy, speed, and consistency are balanced effectively with this hybrid approach.
