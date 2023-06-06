

const predsRaw = '{{data|safe}}'
const preds = JSON.parse(predsRaw)

for (pred in preds) {
    const predictionStr = `${pred}:${preds[pred]}`
    const pElement = document.createElement('p').appendChild(
        document.createTextNode(predictionStr)
    )
    document.getElementById('predictions').appendChild(pElement)
}