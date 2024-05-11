package main

import (
	"context"
	"fmt"
	"go/go/asrclient"
	"io"
	"log"
	"os"

	"github.com/zeromicro/go-zero/zrpc"
)

func main() {

	client := asrclient.NewASR(zrpc.MustNewClient(zrpc.RpcClientConf{
		Target: "dns:///127.0.0.1:8080",
	}))
	f, err := os.Open("./ie.wav")
	if err != nil {
		fmt.Println(err.Error())
	}
	fd, err := io.ReadAll(f)
	if err != nil {
		fmt.Println(err.Error())
	}

	resp, err := client.ASR(context.Background(), &asrclient.AsrRequest{
		Audiobytes: fd,
		Filename:   "ie.wav",
	})
	if err != nil {
		log.Println(err)
		return
	}
	log.Println(resp)

}
