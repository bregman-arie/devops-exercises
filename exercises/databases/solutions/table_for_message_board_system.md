## Database Table for Message Board System

### Instructions

Design a database table for a message board system. It should include the following information:

  * Personal details
  * Who saw the message and when
  * Replies
  * Tagged people in the message
  * Message categories

Notes:

  * No SQL is needed
  * You should include: table names, field names, data types and mention the foreign keys used.

### Solution

Note: This is just one possible design
2nd Note: PK = primary key, FK = Foreign key

                                ----- People -----
                                ID int PK
                                FirstName varchar(255)
                                LastName varchar(255)
                                DOB date
                                Gender varchar(1)
                                Phone varchar(10)

                                       |               \
                                       |                \ 
                                       |                 \
                                       v                  \ 
                                                           \
                                --- Messages ---            v
                                ID int PK
                                MessageBoardID FK             --- MessageTags ---
--- MessageBoards ---           PeopleID int FK               ID int PK
ID int PK              ---->    MsgDate datetime       --->   MessageID FK
Board text                      Message text                  PeopleID int Fk
                                MessageID (FK)
                                       ^      |
                                       |      |
                                       |______|

