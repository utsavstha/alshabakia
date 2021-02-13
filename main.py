from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession

api_id = 3786600
api_hash = '561459bb4863347b4551c5e6f8584dbb'
client = TelegramClient(StringSession("1ApWapzMBu7rfV2wPZKg4TbdUVrzbrPi6V2fR4UO62A0y82SbJM4tYkkpiAbKnRXhNlnH_WbuOGA3Y9BN4TuDHCSA9lh4Zi4gjsxzFHszESJ_u30eGSd_2RZUavKwkOoF-vAHjvGr5PJg8oBe6C0p2RpygdEqD_QdxX0m_gRgpSMYgwvCr-eMhSXZU2N_OG9DOY-IU4Qvsi7rOusgarI_LlD6Ga55R_Wv0sA5_Wd_X0i44SgdvLjawWN-Q_s8Z1ajpzsCkQoz_3-1Ft5UJd5Wq5-vbbsjvwyqHLOoly2bBnFpXNxFJC7fg_VEfOb8lhWdnQO3hjPkMVh7o0sPcQ9nmwsKoh1Z-YE="), api_id, api_hash)
client.start()    
# print(client.session.save())
print("SERVER STARTED")


@client.on(events.NewMessage(chats="shehabtelegram"))
async def my_event_handler(event):
    print("new event")
    if "حماسفلسطين" in event.raw_text or "حماس" in event.raw_text or "فتح" in event.raw_text or "احتلال" in event.raw_text or "غزه" in event.raw_text or "خان يونس " in event.raw_text or "معبر رفح " in event.raw_text or "حماس" in event.raw_text or "رفح" in event.raw_text or "الجهاد الاسلامي " in event.raw_text or "انفاق" in event.raw_text:
            print("Posted from shehabtelegram")
            await client.send_message('alshabakia', event.raw_text)

@client.on(events.NewMessage(chats="gazanewsnow"))
async def my_event_handler(event):
    print("new event")
    if "حماسفلسطين" in event.raw_text or "حماس" in event.raw_text or "فتح" in event.raw_text or "احتلال" in event.raw_text or "غزه" in event.raw_text or "خان يونس " in event.raw_text or "معبر رفح " in event.raw_text or "حماس" in event.raw_text or "رفح" in event.raw_text or "الجهاد الاسلامي " in event.raw_text or "انفاق" in event.raw_text:
            print("Posted from gazanewsnow")
            await client.send_message('alshabakia', event.raw_text)

@client.on(events.NewMessage(chats="ajMubasher"))
async def my_event_handler(event):
    print("new event")
    if "حماسفلسطين" in event.raw_text or "حماس" in event.raw_text or "فتح" in event.raw_text or "احتلال" in event.raw_text or "غزه" in event.raw_text or "خان يونس " in event.raw_text or "معبر رفح " in event.raw_text or "حماس" in event.raw_text or "رفح" in event.raw_text or "الجهاد الاسلامي " in event.raw_text or "انفاق" in event.raw_text:
            print("Posted from ajMubasher")
            await client.send_message('alshabakia', event.raw_text)

@client.on(events.NewMessage(chats="ajanews"))
async def my_event_handler(event):
    print("new event")
    if "حماسفلسطين" in event.raw_text or "حماس" in event.raw_text or "فتح" in event.raw_text or "احتلال" in event.raw_text or "غزه" in event.raw_text or "خان يونس " in event.raw_text or "معبر رفح " in event.raw_text or "حماس" in event.raw_text or "رفح" in event.raw_text or "الجهاد الاسلامي " in event.raw_text or "انفاق" in event.raw_text:
            print("Posted from ajanews")
            await client.send_message('alshabakia', event.raw_text)

@client.on(events.NewMessage(chats="hamasps"))
async def my_event_handler(event):
    print("new event")
    if "حماسفلسطين" in event.raw_text or "حماس" in event.raw_text or "فتح" in event.raw_text or "احتلال" in event.raw_text or "غزه" in event.raw_text or "خان يونس " in event.raw_text or "معبر رفح " in event.raw_text or "حماس" in event.raw_text or "رفح" in event.raw_text or "الجهاد الاسلامي " in event.raw_text or "انفاق" in event.raw_text:
            print("Posted from hamasps")
            await client.send_message('alshabakia', event.raw_text)


with client:
    client.run_until_disconnected()


