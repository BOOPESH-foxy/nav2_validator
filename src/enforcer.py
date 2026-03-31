# Enforcer: orchestrates extraction, comparison, and reporting
# Logic will be implemented in tasks 5.1 and 6.1

from dataclasses import dataclass, field


@dataclass
class ComplianceResult:
    cpp_file: str
    md_file: str
    undocumented: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return len(self.undocumented) == 0


def check_plugin(cpp_file: str, md_file: str) -> ComplianceResult:
    """Compare parameters from cpp_file against those documented in md_file."""
    raise NotImplementedError


def run(plugin_pairs: list[tuple[str, str]]) -> int:
    """Run enforcer over (cpp_file, md_file) pairs. Returns exit code 0, 1, or 2."""
    raise NotImplementedError


if __name__ == "__main__":
    raise NotImplementedError
