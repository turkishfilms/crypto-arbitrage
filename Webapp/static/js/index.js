

const fillArbTableData = (spots) => {
    const table = document.getElementById('table')
    spots.forEach(spot => {
        const row = table.insertRow(-1)
        let counter = 0
        for (key in spot) {
            const cell = row.insertCell(counter)
            cell.textContent = spot[key]
            counter++
        }
        const cell5 = row.insertCell(counter)
        cell5.textContent = spot.buyPrice - spot.sellPrice
    })
}

const rawData = "{{data | safe}}"
const data = rawData.replace(/'/g, '"');
const spots = JSON.parse(data)

fillArbTableData(spots)