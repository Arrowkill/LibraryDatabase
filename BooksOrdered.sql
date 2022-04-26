SELECT Vendor_Order_Item.ItemOrderID, 
Vendor_Order_Item.VendorID, 
Vendor_Order_Item.OrderID, 
Vendor_Order_Item.BookID, 
Vendor_Order_Item.Quantity,
Vendor_Order_Item.CreatedOn,
Books.Title,
Books.Author,
Books.Genre,
Books.ISBN
FROM Vendor_Order_Item
INNER JOIN Books ON Vendor_Order_Item.BookID = Books.BookID
WHERE Vendor_Order_Item.BookID = Books.BookID
AND Vendor_Order_Item.BookID IS NOT NULL