import protoLoader from '@grpc/proto-loader'
import grpc from '@grpc/grpc-js'
import path from 'path'

const filename = path.resolve(`./protos/countries.proto`)
const packageDefinination = protoLoader.loadSync(filename, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

const countries = grpc.loadPackageDefinition(packageDefinination)

export default countries
