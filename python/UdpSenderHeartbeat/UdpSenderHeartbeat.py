#--------------------------------------------------------------------------------
# Purpose: Simple utility script to send heartbeat message to ActiveMq broker
#
# Use: python UdpSenderHeartbeat.py
#
# Modification History:
# CR        Date           Name           Comment
# --------  ------------   ------------   ---------------------------------------
# 0000      19/11/2021     amsilva       Initial version
#--------------------------------------------------------------------------------

import socket
import time

#IP and port to send the message
IP = "127.0.0.1"
PORT = 25002


"""
Message format:

xx xx xx xx Destination
xx xx xx xx Source
xx			Protocol
xx xx xx xx Tx Timestamp
xx xx xx xx Sequence Number
xx xx xx xx PDV
xx xx		Data Lenght
xx			Application Data
xx xx xx xx CRC

8 bits   (1 byte)  -> xx
16 bits  (2 bytes) -> xx xx
24 bits  (3 bytes) -> xx xx xx
32 bits  (4 bytes) -> xx xx xx xx

"""

# Minimum values for the message fields
MESSAGE_MinSource = bytearray([0x00,0x00,0x00,0x01])
MESSAGE_MinDest = bytearray([0x00,0x00,0x00,0x01])
MESSAGE_MinProtocol = bytearray([0x00,0x00])
MESSAGE_MinTxTmStmp = bytearray([0x00,0x00,0x00,0x00])
MESSAGE_MinPDV = bytearray([0x00,0x00,0x00,0x00])
MESSAGE_MinDataLen = bytearray([0x00,0x00])
MESSAGE_MinAppData = bytearray([0x02])
MESSAGE_MinCRC = bytearray([0x00,0x00,0x00,0x00])

#Maximum values for the message fields
MESSAGE_MaxSource = bytearray([0xFF,0xFF,0xFF,0xFF])
MESSAGE_MaxDest = bytearray([0xFF,0xFF,0xFF,0xFF])
MESSAGE_MaxProtocol = bytearray([0xFF,0xFF])
MESSAGE_MaxTxTmStmp = bytearray([0xFF,0xFF,0xFF,0xFF])
MESSAGE_MaxPDV = bytearray([0xFF,0xFF,0xFF,0xFF])
MESSAGE_MaxDataLen = bytearray([0xFF,0xFF])
MESSAGE_MaxAppData = bytearray([0xFF])
MESSAGE_MaxCRC = bytearray([0xFF,0xFF,0xFF,0xFF])

#Second most significant byte = 1
MESSAGE_EndSource = bytearray([0x00,0x01,0x00,0x01])
MESSAGE_EndDest = bytearray([0x00,0x00,0x00,0x01])
MESSAGE_EndProtocol = bytearray([0x00,0x00])
MESSAGE_EndTxTmStmp = bytearray([0x00,0x00,0x00,0x00])
MESSAGE_EndPDV = bytearray([0x00,0x00,0x00,0x00])
MESSAGE_EndDataLen = bytearray([0x00,0x00])
MESSAGE_EndAppData = bytearray([0x02])
MESSAGE_EndCRC = bytearray([0x00,0x00,0x00,0x00])

#Complete message
MESSAGE_MIN = MESSAGE_MinSource + MESSAGE_MinDest + MESSAGE_MinProtocol + MESSAGE_MinTxTmStmp + MESSAGE_MinPDV + MESSAGE_MinDataLen + MESSAGE_MinAppData + MESSAGE_MinCRC
MESSAGE_MAX = MESSAGE_MaxSource + MESSAGE_MaxDest + MESSAGE_MaxProtocol + MESSAGE_MaxTxTmStmp + MESSAGE_MaxPDV + MESSAGE_MaxDataLen + MESSAGE_MaxAppData + MESSAGE_MaxCRC
MESSAGE_END = MESSAGE_EndSource + MESSAGE_EndDest + MESSAGE_EndProtocol + MESSAGE_EndTxTmStmp + MESSAGE_EndPDV + MESSAGE_EndDataLen + MESSAGE_EndAppData + MESSAGE_EndCRC


#Send the message for the mininum values and close the socket
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s1.sendto(MESSAGE_MIN, (IP, PORT))
s1.close()

#wait 1 second
time.sleep(1)

#Send the message for the maximum values and close the socket
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s2.sendto(MESSAGE_MAX, (IP, PORT))
s2.close()

#wait 1 second
time.sleep(1)

#send the message for endian values
s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s3.sendto(MESSAGE_END, (IP, PORT))
s3.close()