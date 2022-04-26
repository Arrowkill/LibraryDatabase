SELECT Vendor_Order_Item.ItemOrderID, 
Vendor_Order_Item.VendorID, 
Vendor_Order_Item.OrderID, 
Vendor_Order_Item.ReferenceMaterialID, 
Vendor_Order_Item.Quantity,
Vendor_Order_Item.CreatedOn,
Reference_Material.Title,
Reference_Material.Author
FROM Vendor_Order_Item
INNER JOIN Reference_Material ON Vendor_Order_Item.ReferenceMaterialID = Reference_Material.ReferenceID
WHERE Vendor_Order_Item.ReferenceMaterialID = Reference_Material.ReferenceID
AND Vendor_Order_Item.ReferenceMaterialID IS NOT NULL