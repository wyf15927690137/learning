import axios from 'axios'

const service = axios.create({
    timeout:9999
})

export default service