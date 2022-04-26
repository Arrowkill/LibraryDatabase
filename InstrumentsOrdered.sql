SELECT Vendor_Order_Item.ItemOrderID, 
Vendor_Order_Item.VendorID, 
Vendor_Order_Item.OrderID, 
Vendor_Order_Item.InstrumentID, 
Vendor_Order_Item.Quantity,
Vendor_Order_Item.CreatedOn,
Instruments.Instrument,
Instruments.InstrumentCondition,
Instruments.Accessories
FROM Vendor_Order_Item
INNER JOIN Instruments ON Vendor_Order_Item.InstrumentID = Instruments.InstrumentID
WHERE Vendor_Order_Item.InstrumentID = Instruments.InstrumentID
AND Vendor_Order_Item.InstrumentID IS NOT NULL