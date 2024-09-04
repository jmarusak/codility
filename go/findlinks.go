package main

import (
	"os"
	"fmt"
	"golang.org/x/net/html"
	"net/http"
)

func visit(links []string, n *html.Node) []string {
	if n.Type == html.ElementNode && n.Data == "a" {
		for _, a := range n.Attr {
			if a.Key == "href" {
				links = append(links, a.Val)
			}
		}
	}
	for c := n.FirstChild; c != nil; c = c.NextSibling {
		links = visit(links, c)
	}
	return links
}

func findLinks(url string) ([]string, error) {
	resp, err := http.Get(url)
	if err != nil {
		resp.Body.Close()
		return nil, fmt.Errorf("getting url %v failed: %v", url, err)
	}

	doc, err := html.Parse(resp.Body)
	resp.Body.Close()
	if err != nil {
		return nil, fmt.Errorf("parsing html failed: %v", err)
	}

	return visit(nil, doc), nil
}

func main() {
	url := "https://www.gopl.io/reviews.html"

	links, err := findLinks(url)
	if err != nil {
		fmt.Fprintf(os.Stderr, "findlink: %v\n",  err)
		os.Exit(1)
	}

	for _, link := range links {
		fmt.Println(link)
	}
}
