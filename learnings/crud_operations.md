# CRUD operations

CRUD stands for Create, Read, Update, and Delete, which are the four basic operations that can be performed on data in a database.

In the context of DynamoDB, here's how these CRUD operations are performed:

1. Create: To create a new item in a DynamoDB table, you can use the `PutItem` API. This API allows you to specify the table name, the primary key values for the item, and the attribute values for the item.
2. Read: To read an item from a DynamoDB table, you can use the `GetItem` API. This API allows you to specify the table name and the primary key values for the item you want to retrieve.
3. Update: To update an item in a DynamoDB table, you can use the `UpdateItem` API. This API allows you to specify the table name, the primary key values for the item, and the new attribute values that you want to set.
4. Delete: To delete an item from a DynamoDB table, you can use the `DeleteItem` API. This API allows you to specify the table name and the primary key values for the item you want to delete.

In addition to these basic CRUD operations, DynamoDB also provides additional APIs for querying and scanning tables, batch operations for performing multiple CRUD operations in a single API call, and transactional APIs for performing multiple CRUD operations in a single transaction.
