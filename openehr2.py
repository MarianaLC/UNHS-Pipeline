from base64 import encode
import json
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["local"]
mycol = mydb["OPENEHR"]


#openehr = open("openehr.json","w",encoding='utf-8')
dic = {"Universar Newborn Hearing Screening": {"content": {"Birth Registration RANU":
{"data":
{"Pregnancy":
{"Pregnancy Duration":"/content[openEHR-EHR-EVALUATION.pregnancy_summary_ranu.v0]/data[at0001]/items[at0128]/items[at0141]","Puerperium":"/content[openEHR-EHR-EVALUATION.pregnancy_summary_ranu.v0]/data[at0001]/items[at0128]/items[at0240]"},"Childbirth":{"Place of Birth Category":"/content[openEHR-EHR-EVALUATION.pregnancy_summary_ranu.v0]/data[at0001]/items[at0065]/items[at0117]"},"Newborn":{"Date/Time of Birth":"/content[openEHR-EHR-EVALUATION.pregnancy_summary_ranu.v0]/data[at0001]/items[at0028]/items[at0029]","Sex":"/content[openEHR-EHR-EVALUATION.pregnancy_summary_ranu.v0]/data[at0001]/items[at0028]/items[at0037]","Birthweight":"/content[openEHR-EHR-EVALUATION.pregnancy_summary_ranu.v0]/data[at0001]/items[at0028]/items[at0038]"}},
"protocol":
{"Patient ID":"/content[openEHR-EHR-EVALUATION.pregnancy_summary_ranu.v0]/protocol[at0081]/items[at0243]","Process ID":"/content[openEHR-EHR-EVALUATION.pregnancy_summary_ranu.v0]/protocol[at0081]/items[at0244]"}},
"Deafness Risk Factor in Newborn":
{"data":
{"Risk Factors":{"Risk Factor":"/content[openEHR-EHR-EVALUATION.health_risk_lara_copy.v1, 'Deafness Risk Factors in Newborn']/data[at0001]/items[at0016]/items[at0013]"},
"screening date":"/content[openEHR-EHR-EVALUATION.health_risk_lara_copy.v1, 'Deafness Risk Factors in Newborn']/data[at0001]/items[at0050]",
"risk":"/content[openEHR-EHR-EVALUATION.health_risk_lara_copy.v1, 'Deafness Risk Factors in Newborn']/data[at0001]/items[at0052]"}
,
"protocol":
{"evaluator ID":"/content[openEHR-EHR-EVALUATION.health_risk_lara_copy.v1, 'Deafness Risk Factors in Newborn']/protocol[at0048]/items[at0051]"}},
"Apgar Score":{"data":{"1 minute":{"data":{"Total":"/content[openEHR-EHR-OBSERVATION.apgar_ranu.v2, 'Apgar Score']/data[at0002]/events[at0003]/data[at0001]/items[at0025]"}},"5 minute":{"data":{"Total":"/content[openEHR-EHR-OBSERVATION.apgar_ranu.v2, 'Apgar Score']/data[at0002]/events[at0028]/data[at0001]/items[at0025]"}}}},
"Phase 1":{"data":
{"evaluation":"/content[openEHR-EHR-EVALUATION.phase.v0, 'Phase 1']/data[at0001]/items[at0010]","evaluation date":"/content[openEHR-EHR-EVALUATION.phase.v0, 'Phase 1']/data[at0001]/items[at0007]"},
"protocol":{"evaluator ID":"/content[openEHR-EHR-EVALUATION.phase.v0, 'Phase 1']/protocol[at0008]/items[at0009]"}},
"Phase 2":{"data":
{"evaluation":"/content[openEHR-EHR-EVALUATION.phase.v0, 'Phase 2']/data[at0001]/items[at0010]","evaluation date":"/content[openEHR-EHR-EVALUATION.phase.v0, 'Phase 2']/data[at0001]/items[at0007]"},
"protocol":{"evaluator ID":"/content[openEHR-EHR-EVALUATION.phase.v0, 'Phase 2']/protocol[at0008]/items[at0009]"}},
"Phase 3":{"data":
{"evaluation":"/content[openEHR-EHR-EVALUATION.phase.v0, 'Phase 3']/data[at0001]/items[at0010]","evaluation date":"/content[openEHR-EHR-EVALUATION.phase.v0, 'Phase 3']/data[at0001]/items[at0007]"},
"protocol":{"evaluator ID":"/content[openEHR-EHR-EVALUATION.phase.v0, 'Phase 3']/protocol[at0008]/items[at0009]"}}}}}
#json.dump(dic,openehr,ensure_ascii= False,indent=4)
mycol.insert_one(dic)
