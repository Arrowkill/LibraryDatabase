SELECT Vendor_Order_Item.ItemOrderID, 
Vendor_Order_Item.VendorID, 
Vendor_Order_Item.OrderID, 
Vendor_Order_Item.ConsoleID, 
Vendor_Order_Item.Quantity,
Vendor_Order_Item.CreatedOn,
Consoles.ConsoleDescription
FROM Vendor_Order_Item
INNER JOIN Consoles ON Vendor_Order_Item.ConsoleID = Consoles.ConsoleID
WHERE Vendor_Order_Item.ConsoleID = Consoles.ConsoleID
AND Vendor_Order_Item.ConsoleID IS NOT NULL