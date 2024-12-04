import { createClient } from 'redis';
const express = require('express');

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

let listProducts = [
  {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
  {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
  {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
  {id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
];

function getItemById(id, listProducts) {
  for (const data of listProducts) {
    if (data.id === id) {
      return data;
    }
  }

  return null;
}

function reserveStockById(itemId, stock) {
  client.hset(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
  return await client.get(itemId, (err) => {
    if (err) {
     console.error('Product not found');
    }
  });
}

const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  let items[listProducts.length];
  for (const data of listProducts) {
    items.push({itemId: data.id, itemName: data.name, price: data.price, initialAvailableQuantity: data.stock});
  }
  res.json(items);
});

app.get('/reserve_product/:itemId', (req, res) {
  const id = req.params.get('itemId');
  const item = getItemById(id, listProducts);
  const inStock = getCurrentReservedStockById(id);
  if (!item) {
    return res.json({"status":"Product not found"});
  }

  if (!inStock || inStock < 1) {
    return res.json({"status": "Not enough stock available","itemId": id});
  }

  return res.json({
    "itemId": req.params.get('itemId'),
    "itemName": item.name,
    "price": item.price,
    "initialAvailableQuantity": item.stock,
    "currentQuantity": inStock
  });
});
