// The list of city records
const list = [
  { name: "Lagos", population: 21.0 },
  { name: "Cairo", population: 15.2 },
  { name: "Kinshasa-Brazzaville", population: 11.3 },
  { name: "Greater Johannesburg", population: 7.55 },
  { name: "Mogadishu", population: 5.85 },
  { name: "Khartoum-Omdurman", population: 4.98 },
  { name: "Dar Es Salaam", population: 4.7 },
  { name: "Alexandria", population: 4.58 },
  { name: "Abidjan", population: 4.4 },
  { name: "Casablanca", population: 4.27 },
  { name: "Accra", population: 4.0 },
  { name: "Dakar", population: 3.5 },
  { name: "Addis Ababa", population: 3.4 }
];

function searchCity(cityName) {
  // Find the index of the record where name matches cityName
  for (let i = 0; i < list.length; i++) {
    if (list[i].name === cityName) {
      return i;
    }
  }
  return -1; // Not found
}
