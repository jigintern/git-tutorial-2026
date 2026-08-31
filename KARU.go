package main

import (
	"fmt"
	"math/rand"
	"time"
)

// Go 1.20+ はデフォルトでランダムにシードされるため rand.Seed は不要

var excuses = []string{
	"コンパイルは通ってた",
	"さっきまで動いてた",
	"git pull したらバグった",
	"環境のせい",
	"Wi-Fiのせい",
	"月のせい",
}

func main() {
	fmt.Println("KARU がファーストコミットに挑戦しています...")
	steps := []string{"git init", "git add KARU.go", "git commit -m \"はじめてのコミット\""}

	for _, s := range steps {
		fmt.Printf("$ %s\n", s)
		time.Sleep(300 * time.Millisecond)
	}

	if rand.Intn(2) == 0 {
		fmt.Println("\n✅ コミット成功!KARU、一歩前進。")
	} else {
		fmt.Println("\n❌ コンフリクトが発生しました。")
		fmt.Printf("KARU「%s」\n", excuses[rand.Intn(len(excuses))])
	}
}
