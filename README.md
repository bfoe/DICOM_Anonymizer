# DICOM_Anonymizer
Quick and dirty hack to anonymize DICOM files

This program will modify all DICOM files under the current folder
The following tags will be anonimized::
- PatientName
- PatientBirthDate
- PatientSex
- PatientAge

Files named DICOMDIR can not be modified (however these do contain patient information), non-DICOM files will not be modified (please use other means to anonimyze these)
