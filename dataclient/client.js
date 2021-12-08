import grpc from '@grpc/grpc-js'
import countriesGRPC from './countryGRPC.js'

const query = (country, { client }) => {
  const request = {
    requestBody: JSON.stringify({
      country
    })
  }

  return new Promise((resolve, reject) => {
    return client.getCountries(request, (error, data) => {
      if (error) {
        return reject(error)
      } else {
        return resolve(data)
      }
    })
  })
}

const main = async () => {
  const country = process.argv.slice(2)[0] ?? null

  if (country) {
    const client = new countriesGRPC.Countries('localhost:50051', grpc.credentials.createInsecure())
    const data = await query(country, {client}).then(response => {
      return JSON.parse(response.data)
    })

    console.log(
      JSON.stringify(data, null, 2)
    )
  } else {
    console.error('no search provided')
  }
}

main()
