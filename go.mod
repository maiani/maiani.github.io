module github.com/maiani/maiani_webpage

go 1.24

require github.com/hugo-toha/toha/v4 v4.16.0 // indirect

// Use the local fork checkout so the site can ship theme features ahead of an
// upstream Toha release. CI clones github.com/maiani/toha into ../toha before
// building (see .github/workflows). Drop this replace to return to upstream.
replace github.com/hugo-toha/toha/v4 => ../toha
