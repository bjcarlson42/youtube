import '../styles/globals.css'
import { ChakraProvider } from "@chakra-ui/core"
import customTheme from '../styles/theme'

function MyApp({ Component, pageProps }) {
  return <>
    <ChakraProvider theme={customTheme}>
      <Component {...pageProps} />
    </ChakraProvider>
  </>
}

export default MyApp
