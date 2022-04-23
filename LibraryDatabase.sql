create table Patron (
	FirstName varchar(256) not null,
    LastName varchar(256) not null,
    DateOfBirth date not null,
    Email varchar(256) not null,
    Address varchar(256) not null,
    PatronID varchar(256) not null,
    PhoneNumber varchar(16) not null,
    primary key (PatronID)
);
create table Library_Staff (
	EmployeeFirstName varchar(256) not null,
    EmployeeLastName varchar(256) not null,
    EmployeeEmail varchar(256) not null,
    EmployeePhoneNumber varchar(16) not null,
    StaffID varchar(64) not null,
    primary key (StaffID)
);
create table CD (
	Title varchar(256) not null,
    Author varchar(256) not null,
    Genre varchar(256) not null,
    IsOut bool not null,
    RentalPeriod varchar(256) not null,
    CDID varchar(64) not null,
    primary key (CDID)
);
create table DVD (
	Title varchar(256) not null,
    Studio varchar(256) not null,
    Genre varchar(256) not null,
    IsOut bool not null,
    RentalPeriod varchar(256) not null,
    DVDID varchar(64),
    primary key (DVDID)
);
create table Magazines (
	Title varchar(256) not null,
    Author varchar(256) not null,
    Genre varchar(256) not null,
    ISSN varchar(64) not null,
    IsOut bool not null,
    RentalPeriod varchar(256) not null,
    MagazineID varchar(64) not null,
    primary key (MagazineID, ISSN)
);
create table VHS_Tapes (
	Title varchar(256) not null,
    Studio varchar(256) not null,
    Genre varchar(256) not null,
    IsOut bool not null,
    RentalPeriod varchar(256) not null,
    VHSID varchar(64) not null,
    primary key (VHSID)
);
create table Reference_Material (
	Title varchar(256) not null,
    Author varchar(256) not null,
    IsOut bool not null,
    RentalPeriod varchar(256) not null,
    ReferenceID varchar(64) not null,
    primary key (ReferenceID)
);
create table Books (
	Title varchar(256) not null,
    Author varchar(256) not null,
    Genre varchar(256) not null,
    ISBN varchar(64) not null,
    IsOut bool not null,
    RentalPeriod varchar(256) not null,
    BookID varchar(64) not null,
    primary key (BookID, ISBN)
);
create table Instruments (
	InstrumentID varchar(64) not null,
    Instrument varchar(256) not null,
    InstrumentCondition blob not null,
    Accessories blob not null,
    IsOut bool not null,
    primary key (InstrumentID)
);
create table Printing (
	PrintID varchar(64) not null,
    PrintCost numeric(9, 2) check (PrintCost > 0),
    PageNumber numeric(4, 0) check (PageNumber > 0),
    Color varchar(256) not null,
    primary key (PrintID)
);
create table Consoles (
	ConsoleID varchar(64) not null,
    ConsoleDescription varchar(256) not null,
    IsOut bool not null,
    TimeSlot time not null,
    primary key (ConsoleID)
);
create table Study_Rooms (
	RoomID varchar(64) not null,
    TimeSlot time not null,
    RoomNumber numeric(3, 0) check (RoomNumber > 0),
    IsOut bool not null,
    primary key (RoomID)
);
create table Vendor (
	VendorID varchar(64) not null,
    Address varchar(256) not null,
    PhoneNumber varchar(16) not null,
    primary key (VendorID)
);
create table Vendor_Order (
	OrderID varchar(64) not null,
    ItemID varchar(64) not null,
    Total numeric(9, 2) check (Total > 0),
    CreatedOn date not null,
    primary key (OrderID)
);
create table Patron_Account (
	AccountID varchar(256) not null,
    AccountPassword varchar(256) not null,
    PastDueItems numeric(2, 0) check (PastDueItems >= 0),
    CheckedOutItems numeric(2, 0) check (CheckedOutItems >= 0),
    Fees numeric(9, 2) check (Fees >= 0),
    primary key (AccountID),
    foreign key (AccountID) references Patron (PatronID) on delete cascade
);
create table Patron_Payment (
	PaymentID varchar(64) not null,
    PatronAccountID varchar(256) not null,
    PaymentAmount numeric(9, 2) check (PaymentAmount >= 0),
    primary key (PaymentID),
    foreign key (PatronAccountID) references Patron_Account (AccountID) on delete cascade
);
create table Rental_Cart (
	CartID varchar(64) not null,
    PatronAccountID varchar(256) not null,
    EmployeeID varchar(64) not null,
    DateTimestamp date not null,
    AmountDue numeric(9, 2) check (AmountDue >= 0),
    Note blob,
    primary key (CartID),
    foreign key (EmployeeID) references Library_Staff (StaffID) on delete cascade,
    foreign key (PatronAccountID) references Patron_Account (AccountID) on delete cascade
);
create table Rental_Item (
	RentalID varchar(64) not null,
    CartID varchar(64) not null,
    CDID varchar(64),
    DVDID varchar(64),
    MagazineID varchar(64),
    VHSID varchar(64),
    ReferenceMaterialID varchar(64),
    BookID varchar(64),
    InstrumentID varchar(64),
    ConsoleID varchar(64),
    RoomID varchar(64),
    PrintID varchar(64),
    RentalType varchar(256) not null,
    DueDate date not null,
    primary key (RentalID),
    foreign key (CartID) references Rental_Cart (CartID) on delete cascade,
    foreign key (CDID) references CD (CDID) on delete cascade,
    foreign key (DVDID) references DVD (DVDID) on delete cascade,
    foreign key (MagazineID) references Magazines (MagazineID) on delete cascade,
    foreign key (VHSID) references VHS_Tapes (VHSID) on delete cascade,
    foreign key (ReferenceMaterialID) references Reference_Material (ReferenceID) on delete cascade,
    foreign key (BookID) references Books (BookID) on delete cascade,
    foreign key (InstrumentID) references Instruments (InstrumentID) on delete cascade,
    foreign key (ConsoleID) references Consoles (ConsoleID) on delete cascade,
    foreign key (RoomID) references Study_Rooms (RoomID) on delete cascade,
    foreign key (PrintID) references Printing (PrintID) on delete cascade
);
create table Library_Event (
	EventID varchar(64) not null,
    StaffID varchar(64) not null,
    EventType varchar(256) not null,
    EventFrequencyNumber numeric(6, 0) check (EventFrequencyNumber > 0),
    EventFrequencyUnit varchar(32) not null,
    primary key (EventID),
    foreign key (StaffID) references Library_Staff (StaffID) on delete cascade
);
create table Library_Payment (
	LibraryPaymentID varchar(64) not null,
    EmployeeID varchar(64) not null,
    Address varchar(256) not null,
    PhoneNumber varchar(16) not null,
    PaymentAmount numeric(9, 2) check (PaymentAmount > 0),
    primary key (LibraryPaymentID),
    foreign key (EmployeeID) references Library_Staff (StaffID) on delete cascade
);
create table Donation (
	DonationID varchar(64) not null,
    EmployeeID varchar(64) not null,
	CDID varchar(64),
    DVDID varchar(64),
    MagazineID varchar(64),
    VHSID varchar(64),
    ReferenceMaterialID varchar(64),
    BookID varchar(64),
    InstrumentID varchar(64),
    ConsoleID varchar(64),
    ItemDescription varchar(256) not null,
    ItemCondition blob not null,
    primary key (DonationID),
    foreign key (EmployeeID) references Library_Staff (StaffID) on delete cascade,
    foreign key (CDID) references CD (CDID) on delete cascade,
    foreign key (DVDID) references DVD (DVDID) on delete cascade,
    foreign key (MagazineID) references Magazines (MagazineID) on delete cascade,
    foreign key (VHSID) references VHS_Tapes (VHSID) on delete cascade,
    foreign key (ReferenceMaterialID) references Reference_Material (ReferenceID) on delete cascade,
    foreign key (BookID) references Books (BookID) on delete cascade,
    foreign key (InstrumentID) references Instruments (InstrumentID) on delete cascade,
    foreign key (ConsoleID) references Consoles (ConsoleID) on delete cascade
);
create table Vendor_Order_Item (
	ItemOrderID varchar(64) not null,
    VendorID varchar(64) not null,
    OrderID varchar(64) not null,
    CDID varchar(64),
    DVDID varchar(64),
    MagazineID varchar(64),
    VHSID varchar(64),
    ReferenceMaterialID varchar(64),
    BookID varchar(64),
    InstrumentID varchar(64),
    ConsoleID varchar(64),
    Quantity numeric(2, 0) check (Quantity > 0),
    CreatedOn date not null,
    primary key (ItemOrderID),
    foreign key (VendorID) references Vendor (VendorID) on delete cascade,
    foreign key (OrderID) references Vendor_Order(OrderID) on delete cascade,
    foreign key (CDID) references CD (CDID) on delete cascade,
    foreign key (DVDID) references DVD (DVDID) on delete cascade,
    foreign key (MagazineID) references Magazines (MagazineID) on delete cascade,
    foreign key (VHSID) references VHS_Tapes (VHSID) on delete cascade,
    foreign key (ReferenceMaterialID) references Reference_Material (ReferenceID) on delete cascade,
    foreign key (BookID) references Books (BookID) on delete cascade,
    foreign key (InstrumentID) references Instruments (InstrumentID) on delete cascade,
    foreign key (ConsoleID) references Consoles (ConsoleID) on delete cascade
);
