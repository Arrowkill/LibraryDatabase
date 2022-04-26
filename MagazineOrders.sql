SELECT Vendor_Order_Item.ItemOrderID, 
Vendor_Order_Item.VendorID, 
Vendor_Order_Item.OrderID, 
Vendor_Order_Item.MagazineID, 
Vendor_Order_Item.Quantity,
Vendor_Order_Item.CreatedOn,
Magazines.Title,
Magazines.Author,
Magazines.Genre,
Magazines.ISSN
FROM Vendor_Order_Item
INNER JOIN Magazines ON Vendor_Order_Item.MagazineID = Magazines.MagazineID
WHERE Vendor_Order_Item.MagazineID = Magazines.MagazineID
AND Vendor_Order_Item.MagazineID IS NOT NULL