SELECT Vendor_Order_Item.ItemOrderID, 
Vendor_Order_Item.VendorID, 
Vendor_Order_Item.OrderID, 
Vendor_Order_Item.VHSID, 
Vendor_Order_Item.Quantity,
Vendor_Order_Item.CreatedOn,
VHS_Tapes.Title,
VHS_Tapes.Studio,
VHS_Tapes.Genre
FROM Vendor_Order_Item
INNER JOIN VHS_Tapes ON Vendor_Order_Item.VHSID = VHS_Tapes.VHSID
WHERE Vendor_Order_Item.VHSID = VHS_Tapes.VHSID
AND Vendor_Order_Item.VHSID IS NOT NULL