# See LICENSE.incore for details
"""Console script for riscv_ctg."""

import click,os

from riscv_ctg.log import logger
from riscv_ctg.ctg import ctg
from riscv_ctg.__init__ import __version__
from riscv_ctg.constants import env,gen_sign_dataset,gen_usign_dataset
from riscv_isac.cgf_normalize import expand_cgf
# @click.command()
# @click.version_option(prog_name="RISC-V Compliance Test Generator",version=__version__)
# @click.option('--verbose', '-v', default='error', help='Set verbose level', type=click.Choice(['info','error','debug'],case_sensitive=False))
# @click.option('--out-dir', '-d', default='./', type=click.Path(resolve_path=True,writable=True), help='Output directory path')
# @click.option('--randomize','-r', default=False , is_flag='True', help='Randomize Outputs.')
# @click.option('--cgf','-cf',multiple=True,type=click.Path(exists=True,resolve_path=True,readable=True),help="Path to the cgf file(s). Multiple allowed.")
# @click.option('--procs','-p',type=int,default=1,help='Max number of processes to spawn')
# @click.option('--base-isa','-bi',type=click.Choice(['rv32e','rv32i','rv64i']),help="Base ISA string for the tests.")
# @click.option('--flen','-fl',type=click.Choice(['32','64','0']),help="Value of FLEN in\
#         hardware.",default='0')
# @click.option("--inst",type=int,help="Maximum number of Macro Instances per test.")
# @click.option("--z-inx", '-ix', type=bool, default='False', help="If the extensiion is Z*inx then pass True otherwise defaulted to False")

def functioncall():
    verbose = "debug"
    out_dir = "/home/reg/work/zfinx/RV64Zfinx/fcvt.l.s/tests"
    randomize = True
    flen = 32
    cgf = ('/home/reg/tools/riscv-ctg/sample_cgfs/dataset.cgf', '/home/reg/tools/riscv-ctg/sample_cgfs/sample_cgfs_fext/RV64Zfinx/fcvt.l.s.cgf')
    procs = int(1)
    base_isa = "rv64i"
    inst = None
    inxFlag = True
    cli(verbose, out_dir, randomize , cgf,procs,base_isa, flen,inst, inxFlag)
def cli(verbose, out_dir, randomize , cgf,procs,base_isa, flen,inst, inxFlag):
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    if '32' in base_isa:
        xlen = 32
    elif '64' in base_isa:
        xlen = 64
    print(verbose)
    print(out_dir)
    print(randomize)
    print(cgf)
    print(procs)
    print(base_isa)
    print(inst)
    print(flen)
    print(xlen)
    print(inxFlag)
    ctg(verbose, out_dir, randomize ,xlen, int(flen), cgf,procs,base_isa,inst,inxFlag)
print("pre Hello")
functioncall()
print("post Hello")