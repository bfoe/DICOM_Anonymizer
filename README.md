# DICOM_Anonymizer
Quick and dirty hack to anonymize DICOM files

This program will modify all DICOM files under the current folder.
The following tags will be anonimized:
- PatientName
- PatientBirthDate
- PatientSex
- PatientAge

Files named DICOMDIR can not be modified (however these do contain patient information), non-DICOM files will not be modified (please use other means to anonimyze these)

# Disclaimer
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
THE SOFTWARE. 
