## Package Summary

`rxdeps` is a ROS command-line visualization tool for generating PDFs
of ROS package structure and dependencies. It enables you to visualize
package dependencies, including hooks to color based on different status
types.

## Usage

```
Usage: rxdeps [options]

Options:
  -h, --help            show this help message and exit
  -r, --rosmake         color by rosmakeall results
  -s, --review          color by review status
  --size                whether to size by number of depends on 1
  -l, --license         color by license type
  -v                    don't deduplicate dependencies
  --one                 only draw one away from target
  -q, --quiet           quiet (remove links to common packages)
  --hide_single         hide (remove packages without links)
  --rank                layer by maximum dependency depth
  --cluster             group by main subdir
  --color=FILENAME      use color file
  -o FILENAME           output_filename
  --target=PKG_NAMES_LIST,COMMA_SEPERATED
                        target packages
  --stack=STACK_NAMES_LIST,COMMA_SEPERATED
                        target stacks
  --exclude=PKG_NAMES_LIST,COMMA_SEPERATED
                        exclude packages
  --message=full_message_name
                        target_message
```

It will generate a file like below. The default filename is
`deps.pdf`.

## Example Output

[See Full Size\|height="420",width="717"](attachment:rxdeps_graph.png)
![\|height="420",width="717"](attachment:rxdeps_graph.png)
