import logging
import xml.etree.ElementTree as ET

logging.basicConfig(
    filename='json__Yurii.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()


tree = ET.parse(r'C:\Users\BestLaptop\Desktop\groups.xml')
root = tree.getroot()
logger.info("XML-файл успішно завантажено.")

for group in root.findall('group'):
    timing_exbytes = group.find('timingExbytes')
    if timing_exbytes is not None:
        incoming = timing_exbytes.find('incoming')
        group_name = group.find('name').text if group.find('name') is not None else "Unnamed Group"
        if incoming is not None:
            msg = f"Group: {group_name}, incoming: {incoming.text}"
            print(msg)
            logger.info(msg)
        else:
            msg = f"Group: {group_name}, incoming: Не знайдено"
            print(msg)
            logger.info(msg)