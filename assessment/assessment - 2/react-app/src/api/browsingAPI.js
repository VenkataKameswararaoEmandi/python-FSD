import Tshirt from "../assets/images/clothes.jpg";

const productsData = [
  {
    id: 0,
    name: "Tshirt",
    detail: "Clothes mean nothing until someone lives in them.",
    img: Tshirt,
    moreImage: [],
  },
  {
    id: 1,
    name: "Tshirt",
    detail: "Clothes mean nothing until someone lives in them.",
    img: Tshirt,
  },
  {
    id: 2,
    name: "Tshirt",
    detail: "Clothes mean nothing until someone lives in them.",
    img: Tshirt,
  },
  {
    id: 3,
    name: "Tshirt",
    detail: "Clothes mean nothing until someone lives in them.",
    img: Tshirt,
  },
];

export function getBrowsingData() {
  return productsData;
}

export function getProduct(id) {
  let tempProduct = {};
  for (let i = 0; i < productsData.length; i++) {
    if (productsData[i].id === id) {
      return productsData[i];
    }
  }
  return tempProduct;
}
