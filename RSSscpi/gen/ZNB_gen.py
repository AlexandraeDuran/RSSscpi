# -*- coding: utf-8 -*-
# Generated from ZNB_commands_2_70.inp on 2016-08-09 14:56
from SCPI_gen_support import SCPINode, SCPINodeN, SCPIQuery, SCPISet, SCPIBool
from . import Instrument
class ZNB_gen(Instrument):
    class CAL(SCPINode, SCPIQuery):
        """
        `*CAL
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 
        """
        _cmd = "*CAL"
        args = [""]
        
    class CLS(SCPINode, SCPISet):
        """
        `*CLS
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 
        """
        _cmd = "*CLS"
        args = [""]
        
    class ESE(SCPINode, SCPIQuery, SCPISet):
        """
        `*ESE
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 1
        """
        _cmd = "*ESE"
        args = ["1"]
        
    class ESR(SCPINode, SCPIQuery):
        """
        `*ESR
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 
        """
        _cmd = "*ESR"
        args = [""]
        
    class IDN(SCPINode, SCPIQuery):
        """
        `*IDN
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 
        """
        _cmd = "*IDN"
        args = [""]
        
    class IST(SCPINode, SCPIQuery, SCPISet):
        """
        `*IST
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 1
        """
        _cmd = "*IST"
        args = ["1"]
        
    class OPC(SCPINode, SCPIQuery, SCPISet):
        """
        `*OPC
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 
        """
        _cmd = "*OPC"
        args = [""]
        
    class OPT(SCPINode, SCPIQuery):
        """
        `*OPT
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 
        """
        _cmd = "*OPT"
        args = [""]
        
    class PCB(SCPINode, SCPISet):
        """
        `*PCB
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 1
        """
        _cmd = "*PCB"
        args = ["1"]
        
    class PRE(SCPINode, SCPIQuery, SCPISet):
        """
        `*PRE
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 1
        """
        _cmd = "*PRE"
        args = ["1"]
        
    class PSC(SCPINode, SCPIBool):
        """
        `*PSC
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 1, OFF, ON
        """
        _cmd = "*PSC"
        args = ["1", "OFF", "ON"]
        
    class RST(SCPINode, SCPISet):
        """
        `*RST
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 
        """
        _cmd = "*RST"
        args = [""]
        
    class SRE(SCPINode, SCPIQuery, SCPISet):
        """
        `*SRE
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 1
        """
        _cmd = "*SRE"
        args = ["1"]
        
    class STB(SCPINode, SCPIQuery):
        """
        `*STB
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 
        """
        _cmd = "*STB"
        args = [""]
        
    class TRG(SCPINode, SCPISet):
        """
        `*TRG
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 
        """
        _cmd = "*TRG"
        args = [""]
        
    class TST(SCPINode, SCPIQuery):
        """
        `*TST
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 
        """
        _cmd = "*TST"
        args = [""]
        
    class WAI(SCPINode, SCPISet):
        """
        `*WAI
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e65835.htm>`_
        
        Arguments: 
        """
        _cmd = "*WAI"
        args = [""]
        
    class DCL(SCPINode, SCPIQuery, SCPISet):
        """
        `@DCL
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8e04d5566c46494a.htm>`_
        
        Arguments: 
        """
        _cmd = "@DCL"
        args = [""]
        
    class GET(SCPINode, SCPIQuery, SCPISet):
        """
        `@GET
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8e04d5566c46494a.htm>`_
        
        Arguments: 
        """
        _cmd = "@GET"
        args = [""]
        
    class LOC(SCPINode, SCPIQuery, SCPISet):
        """
        `@LOC
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8e04d5566c46494a.htm>`_
        
        Arguments: 
        """
        _cmd = "@LOC"
        args = [""]
        
    class REM(SCPINode, SCPIQuery, SCPISet):
        """
        `@REM
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8e04d5566c46494a.htm>`_
        
        Arguments: 
        """
        _cmd = "@REM"
        args = [""]
        
    class ABORt(SCPINode, SCPISet):
        """
        `ABORt
        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ea9e0c2ff5474211.htm#ID_dd2ff843031772130a00206a0075bedf-1f9dad2503176c760a00206a011f3527-en-US>`_
        
        Arguments: 
        """
        _cmd = "ABORt"
        args = [""]
        
    class CALCulate(SCPINodeN):
        """
        CALCulate
        
        Arguments: 
        """
        _cmd = "CALCulate"
        args = [""]
        
        class CLIMits(SCPINode):
            """
            CALCulate:CLIMits
            
            Arguments: 
            """
            _cmd = "CLIMits"
            args = [""]
            
            class FAIL(SCPINode, SCPIQuery):
                """
                `CALCulate:CLIMits:FAIL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b5d067ff75ce4bc8.htm#ID_eac6ce9afa8821ae0a00206a008389c0-9a887c81fa881c110a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "FAIL"
                args = [""]
                
        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            `CALCulate:DATA
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a9ce754f8a7c483a.htm#ID_40c37a8cfa8829400a00206a00988dcb-6469059ffa8823920a00206a01a6673d-en-US>`_
            
            Arguments: FDATa, MDATa, NCData, SCORr1, SCORr10, SCORr11, SCORr12, SCORr13, SCORr14, SCORr15, SCORr16, SCORr17, SCORr18, SCORr19, SCORr2, SCORr20, SCORr21, SCORr22, SCORr23, SCORr24, SCORr25, SCORr26, SCORr27, SCORr3, SCORr4, SCORr5, SCORr6, SCORr7, SCORr8, SCORr9, SDATa, TSData, UCData
            """
            _cmd = "DATA"
            args = ["FDATa", "MDATa", "NCData", "SCORr1", "SCORr10", "SCORr11", "SCORr12", "SCORr13", "SCORr14", "SCORr15", "SCORr16", "SCORr17", "SCORr18", "SCORr19", "SCORr2", "SCORr20", "SCORr21", "SCORr22", "SCORr23", "SCORr24", "SCORr25", "SCORr26", "SCORr27", "SCORr3", "SCORr4", "SCORr5", "SCORr6", "SCORr7", "SCORr8", "SCORr9", "SDATa", "TSData", "UCData"]
            
            class ALL(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:ALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1a55fa6074b44acc.htm#ID_9bc5567afa8830e10a00206a01031e8d-d6457c53fa882b430a00206a01a6673d-en-US>`_
                
                Arguments: FDATa, MDATa, SDATa
                """
                _cmd = "ALL"
                args = ["FDATa", "MDATa", "SDATa"]
                
            class CALL(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:CALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/342c7b12f0c3425b.htm#ID_50a40c98350a4f350a00206a008806a1-19dffcd1350a48200a00206a01f2dc17-en-US>`_
                
                Arguments: FSIData, SDATa
                """
                _cmd = "CALL"
                args = ["FSIData", "SDATa"]
                
                class CATalog(SCPINode, SCPIQuery):
                    """
                    `CALCulate:DATA:CALL:CATalog
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2eb08e30e3664412.htm#ID_de9ddd49350a59e30a00206a0057b3a3-d34e11d1350a51e40a00206a01f2dc17-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "CATalog"
                    args = [""]
                    
            class CHANnel(SCPINode):
                """
                CALCulate:DATA:CHANnel
                
                Arguments: 
                """
                _cmd = "CHANnel"
                args = [""]
                
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:DATA:CHANnel:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/67f03a3329554429.htm#ID_a6de926b5d2e7b7d0a001ae706ea3d2c-01ff1e255d2e79c70a001ae75392d2c4-en-US>`_
                    
                    Arguments: FDATa, MDATa, SDATa
                    """
                    _cmd = "ALL"
                    args = ["FDATa", "MDATa", "SDATa"]
                    
                class DALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:DATA:CHANnel:DALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/791f30dde0864bcc.htm#ID_ab2c40015d2e7d900a001ae75e144a27-d22c946e5d2e7c290a001ae75392d2c4-en-US>`_
                    
                    Arguments: FDATa, MDATa, SDATa
                    """
                    _cmd = "DALL"
                    args = ["FDATa", "MDATa", "SDATa"]
                    
            class DALL(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:DALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/44cd9ed2bdc14474.htm#ID_6a89a036fa8838a10a00206a00837657-b47c209efa8832c50a00206a01a6673d-en-US>`_
                
                Arguments: FDATa, MDATa, SDATa
                """
                _cmd = "DALL"
                args = ["FDATa", "MDATa", "SDATa"]
                
            class NSWeep(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:DATA:NSWeep
                
                Arguments: SDATa
                """
                _cmd = "NSWeep"
                args = ["SDATa"]
                
                class COUNt(SCPINode, SCPIQuery):
                    """
                    `CALCulate:DATA:NSWeep:COUNt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/df64f664f7c341d7.htm#ID_675c2f06fa8840610a00206a00f5f114-74a998d4fa883a850a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "COUNt"
                    args = [""]
                    
                class FIRSt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:DATA:NSWeep:FIRSt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/db653262bea049c8.htm#ID_6f599dcafa8847e30a00206a01cb4396-4834fe6cfa8842360a00206a01a6673d-en-US>`_
                    
                    Arguments: SDATa
                    """
                    _cmd = "FIRSt"
                    args = ["SDATa"]
                    
                class LAST(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:DATA:NSWeep:LAST
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/68d77cb0c14a4fb8.htm#ID_79dc4d93fa884f650a00206a0014f820-5e0464d9fa8849b80a00206a01a6673d-en-US>`_
                    
                    Arguments: SDATa
                    """
                    _cmd = "LAST"
                    args = ["SDATa"]
                    
            class SGRoup(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:SGRoup
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d70ccd328fe648fb.htm#ID_f487020ffa8857250a00206a0013f6a1-b99c255cfa8851490a00206a01a6673d-en-US>`_
                
                Arguments: FDATa, MDATa, SDATa
                """
                _cmd = "SGRoup"
                args = ["FDATa", "MDATa", "SDATa"]
                
            class STIMulus(SCPINode, SCPIQuery):
                """
                `CALCulate:DATA:STIMulus
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/038ef1cf7a044e85.htm#ID_c099a65ffa885eb70a00206a01a9364f-47a89778fa88590a0a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "STIMulus"
                args = [""]
                
            class TRACe(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:DATA:TRACe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0ccb336efd194e81.htm#ID_c4253b7991da1d150a00206a01d5c62a-8d7fc8c091da15450a00206a00e9ecac-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "TRACe"
                args = ["'string'"]
                
        class DLINe(SCPINode, SCPIQuery, SCPISet):
            """
            `CALCulate:DLINe
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/789e52d0d45d4a05.htm#ID_86597917fa8866680a00206a00b6f794-18a084d6fa88608c0a00206a01a6673d-en-US>`_
            
            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "DLINe"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
            
            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:DLINe:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/92cd9927bed242fd.htm#ID_a1d23145fa886de90a00206a00dd1777-52a9e9affa88684c0a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
        class EYE(SCPINode):
            """
            CALCulate:EYE
            
            Arguments: 
            """
            _cmd = "EYE"
            args = [""]
            
            class DUT(SCPINode):
                """
                CALCulate:EYE:DUT
                
                Arguments: 
                """
                _cmd = "DUT"
                args = [""]
                
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:EYE:DUT:MODE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6ca8e2c5936f4f32.htm#ID_0274b97b88f3a4cf0a001ae769a26a67-9b41492788f3a3b60a001ae77b2dc49c-en-US>`_
                    
                    Arguments: IDEal, MEASured
                    """
                    _cmd = "MODE"
                    args = ["IDEal", "MEASured"]
                    
            class EMPHasis(SCPINode):
                """
                CALCulate:EYE:EMPHasis
                
                Arguments: 
                """
                _cmd = "EMPHasis"
                args = [""]
                
                class CURSor(SCPINode):
                    """
                    CALCulate:EYE:EMPHasis:CURSor
                    
                    Arguments: 
                    """
                    _cmd = "CURSor"
                    args = [""]
                    
                    class POST(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        CALCulate:EYE:EMPHasis:CURSor:POST
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "POST"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class PRE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:EMPHasis:CURSor:PRE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a351e590610f4c6a.htm#ID_e654395088f3a9630a001ae7077aac4c-3929815e88f3a85a0a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "PRE"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:EYE:EMPHasis:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4ab15eb6e85a4698.htm#ID_d20ee38988f3ab190a001ae724d8fb74-1ea2647288f3aa0f0a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class EQUalization(SCPINode):
                """
                CALCulate:EYE:EQUalization
                
                Arguments: 
                """
                _cmd = "EQUalization"
                args = [""]
                
                class CTLE(SCPINode):
                    """
                    CALCulate:EYE:EQUalization:CTLE
                    
                    Arguments: 
                    """
                    _cmd = "CTLE"
                    args = [""]
                    
                    class DC(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:EQUalization:CTLE:DC
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0f9954c9059449af.htm#ID_b689524b88f3aca00a001ae728374b3b-0030282a88f3abb50a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "DC"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class POLE(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        CALCulate:EYE:EQUalization:CTLE:POLE
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "POLE"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class ZERO(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:EQUalization:CTLE:ZERO
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/24a6c5390bcf48fa.htm#ID_b9be79f188f3afcc0a001ae71acd713c-c254643a88f3aee20a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "ZERO"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:EYE:EQUalization:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e583e5a17d6e4940.htm#ID_775ab3ef88f3b28b0a001ae7493b7dd3-f94757af88f3b1620a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class INPut(SCPINode):
                """
                CALCulate:EYE:INPut
                
                Arguments: 
                """
                _cmd = "INPut"
                args = [""]
                
                class BPATtern(SCPINode):
                    """
                    CALCulate:EYE:INPut:BPATtern
                    
                    Arguments: 
                    """
                    _cmd = "BPATtern"
                    args = [""]
                    
                    class TYPE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:INPut:BPATtern:TYPE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ef1c9772c30d4d7f.htm#ID_10eb4f4f88f3b6060a001ae753071b39-63d12f0188f3b4be0a001ae77b2dc49c-en-US>`_
                        
                        Arguments: PRBS, USER
                        """
                        _cmd = "TYPE"
                        args = ["PRBS", "USER"]
                        
                class DRATe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:EYE:INPut:DRATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6864b59265bc43de.htm#ID_e4873c1288f3b7fa0a001ae70118c47d-2d0d85a588f3b6c10a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DRATe"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class LENGth(SCPINode):
                    """
                    CALCulate:EYE:INPut:LENGth
                    
                    Arguments: 
                    """
                    _cmd = "LENGth"
                    args = [""]
                    
                    class BITS(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:INPut:LENGth:BITS
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/863d20d948b348b9.htm#ID_602702a388f3b9fd0a001ae7566b7a2f-d218bf0188f3b8b50a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "BITS"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class PRBS(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:INPut:LENGth:PRBS
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d2d04050e8884a3e.htm#ID_72cf873f88f3bb840a001ae77098e400-fe0ceed588f3ba8a0a001ae77b2dc49c-en-US>`_
                        
                        Arguments: L10, L11, L13, L15, L5, L7, L9
                        """
                        _cmd = "PRBS"
                        args = ["L10", "L11", "L13", "L15", "L5", "L7", "L9"]
                        
                class OLEVel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:EYE:INPut:OLEVel
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f45096e29da04e79.htm#ID_ca75e2ee88f3bd0b0a001ae7542ede44-949d3d0b88f3bc110a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "OLEVel"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class RTIMe(SCPINode):
                    """
                    CALCulate:EYE:INPut:RTIMe
                    
                    Arguments: 
                    """
                    _cmd = "RTIMe"
                    args = [""]
                    
                    class DATA(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:INPut:RTIMe:DATA
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c8c3bdafc68c4800.htm#ID_8562feb988f3bed00a001ae725dbb775-260d8dd888f3bd970a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "DATA"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class THReshold(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:INPut:RTIMe:THReshold
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7f4bb5b9873b47e0.htm#ID_81b7453e88f3c0850a001ae732dbfe67-3db4434d88f3bf8b0a001ae77b2dc49c-en-US>`_
                        
                        Arguments: T1_9, T2_8
                        """
                        _cmd = "THReshold"
                        args = ["T1_9", "T2_8"]
                        
                class ZLEVel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:EYE:INPut:ZLEVel
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f45096e29da04e79.htm#ID_b7097be688f3c2b80a001ae707e97d13-2e70ec3988f3c17f0a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "ZLEVel"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class JITTer(SCPINode):
                """
                CALCulate:EYE:JITTer
                
                Arguments: 
                """
                _cmd = "JITTer"
                args = [""]
                
                class DIRac(SCPINode):
                    """
                    CALCulate:EYE:JITTer:DIRac
                    
                    Arguments: 
                    """
                    _cmd = "DIRac"
                    args = [""]
                    
                    class DELTa(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:JITTer:DIRac:DELTa
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/788ada66fa2f450a.htm#ID_e65431c988f3c44e0a001ae76de5ab43-f6a715a488f3c3730a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "DELTa"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class PROBability(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:JITTer:DIRac:PROBability
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2284bea426ab4156.htm#ID_7d9e7ab788f3c6130a001ae7274c93a0-852452ab88f3c5190a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "PROBability"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class PERiodic(SCPINode):
                    """
                    CALCulate:EYE:JITTer:PERiodic
                    
                    Arguments: 
                    """
                    _cmd = "PERiodic"
                    args = [""]
                    
                    class FREQuency(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:JITTer:PERiodic:FREQuency
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/51c3dd9953a34f92.htm#ID_84def9f088f3c7aa0a001ae730c4c981-62f78fd888f3c6bf0a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "FREQuency"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class MAGNitude(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:JITTer:PERiodic:MAGNitude
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3df49ffe313c40d7.htm#ID_b6feaa0688f3c9400a001ae72a50cd3b-fca046bf88f3c8360a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "MAGNitude"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class PHASe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:JITTer:PERiodic:PHASe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/28c6eea0b51a4c64.htm#ID_d65ac91d88f3cb050a001ae706367712-b9c0a7c088f3c9dc0a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "PHASe"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class RANDom(SCPINode):
                    """
                    CALCulate:EYE:JITTer:RANDom
                    
                    Arguments: 
                    """
                    _cmd = "RANDom"
                    args = [""]
                    
                    class STDDeviation(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:JITTer:RANDom:STDDeviation
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cded83eaa8f04e87.htm#ID_c6d7fcba88f3ccba0a001ae7724c568c-b9b6533588f3cba10a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STDDeviation"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:EYE:JITTer:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e48dcc2fe41f47fe.htm#ID_aff936b988f3ceae0a001ae73e954187-39b5458a88f3cd950a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
                class TYPE(SCPINode):
                    """
                    CALCulate:EYE:JITTer:TYPE
                    
                    Arguments: 
                    """
                    _cmd = "TYPE"
                    args = [""]
                    
                    class DIRac(SCPINode, SCPIBool):
                        """
                        `CALCulate:EYE:JITTer:TYPE:DIRac
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/65f780ce599b421c.htm#ID_295f03fc88f3d0830a001ae7717ba401-d798ae1d88f3cf5a0a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "DIRac"
                        args = ["1", "OFF", "ON"]
                        
                    class PERiodic(SCPINode, SCPIBool):
                        """
                        `CALCulate:EYE:JITTer:TYPE:PERiodic
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/429dd9c2835a48b9.htm#ID_b0a0215d88f3d2390a001ae70a887194-1d5636db88f3d13f0a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "PERiodic"
                        args = ["1", "OFF", "ON"]
                        
                    class RANDom(SCPINode, SCPIBool):
                        """
                        `CALCulate:EYE:JITTer:TYPE:RANDom
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f1ead16a13024b40.htm#ID_8af62ff088f3d3900a001ae7541ce86f-3abf0a9d88f3d2d50a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "RANDom"
                        args = ["1", "OFF", "ON"]
                        
                    class USER(SCPINode, SCPIBool):
                        """
                        `CALCulate:EYE:JITTer:TYPE:USER
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/34ca0da794cf403d.htm#ID_6d13484088f3d66f0a001ae75cf4f504-f58bce7888f3d5750a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "USER"
                        args = ["1", "OFF", "ON"]
                        
            class MASK(SCPINode):
                """
                CALCulate:EYE:MASK
                
                Arguments: 
                """
                _cmd = "MASK"
                args = [""]
                
                class CENTer(SCPINode):
                    """
                    CALCulate:EYE:MASK:CENTer
                    
                    Arguments: 
                    """
                    _cmd = "CENTer"
                    args = [""]
                    
                    class HORizontal(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:MASK:CENTer:HORizontal
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dc4c397db4894718.htm#ID_7b6ffba588f3d7d60a001ae700e9b26b-cde58e1588f3d70b0a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "HORizontal"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class VERTical(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:MASK:CENTer:VERTical
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/311d9091e1e34f17.htm#ID_cfe7728088f3d95d0a001ae70605e411-96ee646d88f3d8630a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "VERTical"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class DATA(SCPINode, SCPIQuery):
                    """
                    `CALCulate:EYE:MASK:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b0646143f63d4d75.htm#ID_7f6b48fe88f3db120a001ae7323fdf81-c99f31b288f3da090a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "DATA"
                    args = [""]
                    
                class FAIL(SCPINode, SCPIQuery):
                    """
                    `CALCulate:EYE:MASK:FAIL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6e8751df0bda477f.htm#ID_23b1ad7888f3dcc80a001ae7662b21ff-8ab3f5dd88f3dbbe0a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "FAIL"
                    args = [""]
                    
                    class BEEP(SCPINode, SCPIBool):
                        """
                        `CALCulate:EYE:MASK:FAIL:BEEP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/591f2624b47b4744.htm#ID_47f2b37f88f3de3f0a001ae7199e5a62-1588540a88f3dd740a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "BEEP"
                        args = ["1", "OFF", "ON"]
                        
                    class CONDition(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:MASK:FAIL:CONDition
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a6f2c3beca684951.htm#ID_e0350fac88f3dfc60a001ae763bc97d6-915144a388f3deeb0a001ae77b2dc49c-en-US>`_
                        
                        Arguments: RATE, SAMPles
                        """
                        _cmd = "CONDition"
                        args = ["RATE", "SAMPles"]
                        
                class SHAPe(SCPINode):
                    """
                    CALCulate:EYE:MASK:SHAPe
                    
                    Arguments: 
                    """
                    _cmd = "SHAPe"
                    args = [""]
                    
                    class BOTTom(SCPINode):
                        """
                        CALCulate:EYE:MASK:SHAPe:BOTTom
                        
                        Arguments: 
                        """
                        _cmd = "BOTTom"
                        args = [""]
                        
                        class HORizontal(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:EYE:MASK:SHAPe:BOTTom:HORizontal
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cf05174ba4fa42a4.htm#ID_a5764ce788f3e14c0a001ae7443ed3a1-3a09e87988f3e0620a001ae77b2dc49c-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "HORizontal"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:EYE:MASK:SHAPe:BOTTom:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3c161bc70d0546de.htm#ID_2eeb5a1b88f3e3020a001ae709c4a9bf-a144e37488f3e1f80a001ae77b2dc49c-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                        class VERTical(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:EYE:MASK:SHAPe:BOTTom:VERTical
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/16ac73dd86a54b09.htm#ID_d4b2b09388f3e4c70a001ae720d63fad-45ef16e388f3e38e0a001ae77b2dc49c-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "VERTical"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                    class POLYgon(SCPINode):
                        """
                        CALCulate:EYE:MASK:SHAPe:POLYgon
                        
                        Arguments: 
                        """
                        _cmd = "POLYgon"
                        args = [""]
                        
                        class HORizontal(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:EYE:MASK:SHAPe:POLYgon:HORizontal
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6fe25873a8624c93.htm#ID_3dd903eb88f3e6ca0a001ae730b8573c-9fc480fb88f3e5920a001ae77b2dc49c-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "HORizontal"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:EYE:MASK:SHAPe:POLYgon:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3c161bc70d0546de.htm#ID_77ed544188f3e8900a001ae7656d3c45-794d176d88f3e7760a001ae77b2dc49c-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                        class TYPE(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:EYE:MASK:SHAPe:POLYgon:TYPE
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6b472744023547a1.htm#ID_a9c13a4c88f3ea350a001ae705930055-1661d47488f3e93b0a001ae77b2dc49c-en-US>`_
                            
                            Arguments: HEXagon, OCTogon, RECTangle
                            """
                            _cmd = "TYPE"
                            args = ["HEXagon", "OCTogon", "RECTangle"]
                            
                        class VERTical(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:EYE:MASK:SHAPe:POLYgon:VERTical
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d774dcb745184296.htm#ID_5d5271b788f3ebbc0a001ae76f7492ad-cc2f698188f3ead20a001ae77b2dc49c-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "VERTical"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                    class TOP(SCPINode):
                        """
                        CALCulate:EYE:MASK:SHAPe:TOP
                        
                        Arguments: 
                        """
                        _cmd = "TOP"
                        args = [""]
                        
                        class HORizontal(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:EYE:MASK:SHAPe:TOP:HORizontal
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cf05174ba4fa42a4.htm#ID_cd06b70988f3ed720a001ae70ea59dd7-1e157ecb88f3ec580a001ae77b2dc49c-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "HORizontal"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:EYE:MASK:SHAPe:TOP:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3c161bc70d0546de.htm#ID_5b345f9688f3ef560a001ae7587f517e-3ff165a788f3ee3d0a001ae77b2dc49c-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                        class VERTical(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:EYE:MASK:SHAPe:TOP:VERTical
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/16ac73dd86a54b09.htm#ID_bba3ff5288f3f10b0a001ae761b47661-b70409f588f3eff20a001ae77b2dc49c-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "VERTical"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                class SHOW(SCPINode, SCPIBool):
                    """
                    `CALCulate:EYE:MASK:SHOW
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/315b9a876d764945.htm#ID_8a4a1e7c88f3f2ff0a001ae7775d8a93-8077f65288f3f1c70a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "SHOW"
                    args = ["1", "OFF", "ON"]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:EYE:MASK:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/fb0d14860aa84736.htm#ID_380db7a688f3f5320a001ae76bef1f4b-9aafcd9f88f3f3bb0a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
                class VIOLation(SCPINode):
                    """
                    CALCulate:EYE:MASK:VIOLation
                    
                    Arguments: 
                    """
                    _cmd = "VIOLation"
                    args = [""]
                    
                    class RATE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:MASK:VIOLation:RATE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/06caefdd3f87445a.htm#ID_289a86a20992843e0a001ae767345ea0-83db806a099282f60a001ae7146ce1d5-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "RATE"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class TOLerance(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:EYE:MASK:VIOLation:TOLerance
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/89eebd5920044714.htm#ID_7185eccb88f3f7260a001ae77ace6488-011cb28088f3f5fd0a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "TOLerance"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
            class MEASurement(SCPINode):
                """
                CALCulate:EYE:MEASurement
                
                Arguments: 
                """
                _cmd = "MEASurement"
                args = [""]
                
                class DATA(SCPINode, SCPIQuery):
                    """
                    `CALCulate:EYE:MEASurement:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ff039718099a4a08.htm#ID_2835221188f3f8eb0a001ae73b78cddb-f59a869b88f3f7f10a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "DATA"
                    args = [""]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:EYE:MEASurement:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1cfafc71d1f54dc7.htm#ID_b10994d688f3fa620a001ae75262b8ca-6e5668bc88f3f9780a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class NOISe(SCPINode):
                """
                CALCulate:EYE:NOISe
                
                Arguments: 
                """
                _cmd = "NOISe"
                args = [""]
                
                class RMS(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:EYE:NOISe:RMS
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/38aff658653a4d80.htm#ID_7402be0388f3fcf20a001ae711ff65dd-efcd09a888f3faef0a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "RMS"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:EYE:NOISe:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/782e358a3e234615.htm#ID_dd48d20f88f3feb80a001ae727ecb1bf-ad10b37588f3fdae0a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:EYE:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8674f76d78df4eb9.htm#ID_9514d2e888f4004e0a001ae72e74247f-d60f0aa588f3ff630a001ae77b2dc49c-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
            class STIMulus(SCPINode):
                """
                CALCulate:EYE:STIMulus
                
                Arguments: 
                """
                _cmd = "STIMulus"
                args = [""]
                
                class ENCoder(SCPINode, SCPIBool):
                    """
                    `CALCulate:EYE:STIMulus:ENCoder
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c612a42ea8fb4ac0.htm#ID_7751a3a688f401b50a001ae751dcf872-a0ae414f88f400cb0a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "ENCoder"
                    args = ["1", "OFF", "ON"]
                    
                class LOWPass(SCPINode, SCPIBool):
                    """
                    `CALCulate:EYE:STIMulus:LOWPass
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/889de7f760b54972.htm#ID_7c06be5988f4033c0a001ae73fe5a6c3-1ebdfd6188f402510a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "LOWPass"
                    args = ["1", "OFF", "ON"]
                    
                class SCRambler(SCPINode, SCPIBool):
                    """
                    `CALCulate:EYE:STIMulus:SCRambler
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/85ef89cb515743bb.htm#ID_fdc378c388f405010a001ae7180ec06d-9b00e1fa88f403e80a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "SCRambler"
                    args = ["1", "OFF", "ON"]
                    
            class VIEW(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:EYE:VIEW
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/812004cf0845412b.htm#ID_009f396888f406f50a001ae726d4ee26-f62f5c0d88f405dc0a001ae77b2dc49c-en-US>`_
                
                Arguments: DUT, EMPHasis, EQUalization, JITTer, NOISe, STIMulus
                """
                _cmd = "VIEW"
                args = ["DUT", "EMPHasis", "EQUalization", "JITTer", "NOISe", "STIMulus"]
                
        class FILTer(SCPINode):
            """
            CALCulate:FILTer
            
            Arguments: 
            """
            _cmd = "FILTer"
            args = [""]
            
            class GATE(SCPINode):
                """
                CALCulate:FILTer:GATE
                
                Arguments: 
                """
                _cmd = "GATE"
                args = [""]
                
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    CALCulate:FILTer:GATE:TIME
                    
                    Arguments: BPASs, NOTCh
                    """
                    _cmd = "TIME"
                    args = ["BPASs", "NOTCh"]
                    
                    class AOFFset(SCPINode, SCPIBool):
                        """
                        `CALCulate:FILTer:GATE:TIME:AOFFset
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/13b7cd6211a64886.htm#ID_76a35f12e2b27f340a00201900691b7c-b24d2b5c9d95c7d60a00201901108bad-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "AOFFset"
                        args = ["1", "OFF", "ON"]
                        
                    class CENTer(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:CENTer
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/708d0e1a2d574ab4.htm#ID_8939aaaffa88756b0a00206a00804a7d-9e5db8b9fa886fce0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "CENTer"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class DCHebyshev(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:DCHebyshev
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/65c43bf8cd18408a.htm#ID_7fba1aeafa887cce0a00206a019b2ba1-e5421c59fa8877500a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "DCHebyshev"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class SHAPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:SHAPe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/54f92ea1195240bc.htm#ID_031b5b73fa88848e0a00206a00b00ed6-d02bdedbfa887ec20a00206a01a6673d-en-US>`_
                        
                        Arguments: MAXimum, MINimum, NORMal, WIDE
                        """
                        _cmd = "SHAPe"
                        args = ["MAXimum", "MINimum", "NORMal", "WIDE"]
                        
                    class SHOW(SCPINode, SCPIBool):
                        """
                        `CALCulate:FILTer:GATE:TIME:SHOW
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/df1959e8b0fc4cc4.htm#ID_5bdd49f3fa888c000a00206a0155fee8-5df0b4aafa8886730a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "SHOW"
                        args = ["1", "OFF", "ON"]
                        
                    class SPAN(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:SPAN
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a9ca210cb08a416a.htm#ID_1f821d5afa8893a20a00206a017ae442-3cf5253bfa888df40a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "SPAN"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:STARt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/76948f89db62434b.htm#ID_839a66a9fa889b620a00206a0160e4c2-22dadc45fa8895960a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STARt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class STATe(SCPINode, SCPIBool):
                        """
                        `CALCulate:FILTer:GATE:TIME:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1222ca1a6262411a.htm#ID_8cc9db0bfa88a2c40a00206a007a16ad-6e3bd764fa889d370a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:STOP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/76948f89db62434b.htm#ID_7956fee9fa88aa560a00206a00a34674-2328ec2afa88a4990a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STOP"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class TYPE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:TYPE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7b8b789f4a4148ec.htm#ID_3e6d61d6fa88b9690a00206a0013cd15-cb383adafa88b39d0a00206a01a6673d-en-US>`_
                        
                        Arguments: BPASs, NOTCh
                        """
                        _cmd = "TYPE"
                        args = ["BPASs", "NOTCh"]
                        
                    class WINDow(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:FILTer:GATE:TIME:WINDow
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/aa512b0a1a7341fc.htm#ID_ef3431c2fa88b1c80a00206a003380d7-10ec9575fa88ac2b0a00206a01a6673d-en-US>`_
                        
                        Arguments: BOHMan, DCHebyshev, HAMMing, HANNing, RECT
                        """
                        _cmd = "WINDow"
                        args = ["BOHMan", "DCHebyshev", "HAMMing", "HANNing", "RECT"]
                        
        class FORMat(SCPINode, SCPIQuery, SCPISet):
            """
            `CALCulate:FORMat
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/132d40cd4d1d43c4.htm#ID_d897b8eafa88c10a0a00206a011a6be4-72cc9cedfa88bb4e0a00206a01a6673d-en-US>`_
            
            Arguments: COMPlex, GDELay, IMAGinary, ISMith, MAGNitude, MLINear, MLOGarithmic, PHASe, POLar, REAL, SMITh, SWR, UPHase
            """
            _cmd = "FORMat"
            args = ["COMPlex", "GDELay", "IMAGinary", "ISMith", "MAGNitude", "MLINear", "MLOGarithmic", "PHASe", "POLar", "REAL", "SMITh", "SWR", "UPHase"]
            
            class WQUType(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:FORMat:WQUType
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f59df8170e2e48b1.htm#ID_58fe9ca9134bbdc10a00206a01c60d6d-3d8b7753134bb65e0a00206a0182dc26-en-US>`_
                
                Arguments: POWer, VOLTage
                """
                _cmd = "WQUType"
                args = ["POWer", "VOLTage"]
                
        class GDAPerture(SCPINode):
            """
            CALCulate:GDAPerture
            
            Arguments: 
            """
            _cmd = "GDAPerture"
            args = [""]
            
            class SCOunt(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:GDAPerture:SCOunt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c736cb18a37c4bcf.htm#ID_71a00580fa88f5e50a00206a0102d135-12afaa0ffa88f0380a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "SCOunt"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
        class LDEViation(SCPINode):
            """
            CALCulate:LDEViation
            
            Arguments: 
            """
            _cmd = "LDEViation"
            args = [""]
            
            class AUTO(SCPINode, SCPISet):
                """
                CALCulate:LDEViation:AUTO
                
                Arguments: ONCE
                """
                _cmd = "AUTO"
                args = ["ONCE"]
                
            class CONStant(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LDEViation:CONStant
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CONStant"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class ELENgth(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LDEViation:ELENgth
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "ELENgth"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class MODE(SCPINode, SCPIBool):
                """
                CALCulate:LDEViation:MODE
                
                Arguments: OFF, ON, TRACking
                """
                _cmd = "MODE"
                args = ["OFF", "ON", "TRACking"]
                
            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LDEViation:SLOPe
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "SLOPe"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
        class LIMit(SCPINodeN):
            """
            CALCulate:LIMit
            
            Arguments: 
            """
            _cmd = "LIMit"
            args = [""]
            
            class CIRCle(SCPINode, SCPIBool):
                """
                CALCulate:LIMit:CIRCle
                
                Arguments: 1, OFF, ON
                """
                _cmd = "CIRCle"
                args = ["1", "OFF", "ON"]
                
                class CLEar(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:CIRCle:CLEar
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1f1b628da0ff4632.htm#ID_0e0cda67e2b28c830a00201900760f22-d4bd05cae2b28b4a0a002019017b841c-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "CLEar"
                    args = [""]
                    
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:CIRCle:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2ed038e078b94e81.htm#ID_00d3a3fdbba6da9f0a002019017a3f54-baaba439bba6d9660a0020190170f726-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class DISPlay(SCPINode, SCPIBool):
                    """
                    CALCulate:LIMit:CIRCle:DISPlay
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "DISPlay"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `CALCulate:LIMit:CIRCle:DISPlay:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/95c25e5e1cc049ad.htm#ID_02d43bf1bba6dc440a002019016ba97e-a3f8e06fbba6db0c0a0020190170f726-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class FAIL(SCPINode, SCPIQuery):
                    """
                    `CALCulate:LIMit:CIRCle:FAIL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3a8b018f1c4549aa.htm#ID_6567a18abba6ddfa0a002019019eee1a-7b3fc002bba6dcb20a0020190170f726-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "FAIL"
                    args = [""]
                    
                    class ALL(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:CIRCle:FAIL:ALL
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/07f68e8133af4d34.htm#ID_2ef23be7a1e90cd10a001ae723a88db3-dab4fe52a1e90b690a001ae70a9caa95-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "ALL"
                        args = ["'string'"]
                        
                class SOUNd(SCPINode, SCPIBool):
                    """
                    CALCulate:LIMit:CIRCle:SOUNd
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "SOUNd"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `CALCulate:LIMit:CIRCle:SOUNd:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/154eb220f88d4f32.htm#ID_bc8304e0bba6dfa00a002019016c88e3-6624d71cbba6de770a0020190170f726-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:LIMit:CIRCle:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/47c20d06725748a5.htm#ID_a38a567ebba6e1550a00201900cb8393-0af63611bba6dffe0a0020190170f726-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class CLEar(SCPINode, SCPISet):
                """
                `CALCulate:LIMit:CLEar
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f3d7c761247b47f0.htm#ID_dc89d368e2b28f900a0020190141c352-f1766415e2b28e570a002019017b841c-en-US>`_
                
                Arguments: 
                """
                _cmd = "CLEar"
                args = [""]
                
            class CONTrol(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:CONTrol
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CONTrol"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:CONTrol:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7fb73b9082124702.htm#ID_8c0418dcfa89330e0a00206a00138405-43be1e80fa892d600a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class DOMain(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:CONTrol:DOMain
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e8aa35068b694faf.htm#ID_b1c1b996fa8923eb0a00206a00a30cbc-432d059efa891e4d0a00206a01a6673d-en-US>`_
                    
                    Arguments: FLIN, FLOG, FSEG, FSINgle, PLIN, PLOG, PSINgle, TLIN, TLOG
                    """
                    _cmd = "DOMain"
                    args = ["FLIN", "FLOG", "FSEG", "FSINgle", "PLIN", "PLOG", "PSINgle", "TLIN", "TLOG"]
                    
                class SHIFt(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:CONTrol:SHIFt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c0acf94a1b904577.htm#ID_e02c13f2fa892b5d0a00206a00d97f61-ac43656dfa8925bf0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "SHIFt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class DATA(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:LIMit:DATA
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e71347.htm#ID_0edb9fe4fa893a8f0a00206a0022bc60-e6fbb4aa4b56d1d50a00206a01a60f5f-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "DATA"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class DCIRcle(SCPINode, SCPIBool):
                """
                CALCulate:LIMit:DCIRcle
                
                Arguments: 1, OFF, ON
                """
                _cmd = "DCIRcle"
                args = ["1", "OFF", "ON"]
                
                class CLEar(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:DCIRcle:CLEar
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4b35d96f647543d5.htm#ID_649bea3342ade7210a001ae77dacf09c-3c7f2a7042ade54c0a001ae769a5b4da-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "CLEar"
                    args = [""]
                    
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:DCIRcle:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e2339de954c84af1.htm#ID_6d2d12e142ade9a10a001ae77edbd9d2-5721e13b42ade7cc0a001ae769a5b4da-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class DISPlay(SCPINode, SCPIBool):
                    """
                    CALCulate:LIMit:DCIRcle:DISPlay
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "DISPlay"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `CALCulate:LIMit:DCIRcle:DISPlay:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ef4c569a517d45b4.htm#ID_f4917f2842adebb40a001ae7609910b4-f3b7ec5742adea2e0a001ae769a5b4da-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:LIMit:DCIRcle:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6ef75dfe0c814d19.htm#ID_d5ff0bb142adeee10a001ae759857318-8dc472fa42adec600a001ae769a5b4da-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class DELete(SCPINode):
                """
                CALCulate:LIMit:DELete
                
                Arguments: 
                """
                _cmd = "DELete"
                args = [""]
                
                class ALL(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:DELete:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7653993fc6474b79.htm#ID_8a7de250fa8942020a00206a002374c5-0bf55881fa893c740a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "ALL"
                    args = [""]
                    
            class DISPlay(SCPINode, SCPIBool):
                """
                CALCulate:LIMit:DISPlay
                
                Arguments: 1, OFF, ON
                """
                _cmd = "DISPlay"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:LIMit:DISPlay:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a620fa8c37b143ad.htm#ID_201695c6fa8949930a00206a0137b8c8-b12eb996fa8943e60a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class FAIL(SCPINode, SCPIQuery):
                """
                `CALCulate:LIMit:FAIL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a70d2fed40134890.htm#ID_f86051f1fa8951150a00206a01cb3196-02514d2afa894b770a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "FAIL"
                args = [""]
                
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:FAIL:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/11aaccb278fd4696.htm#ID_847e9896a1e911e10a001ae76a2c60e0-ebef358aa1e910b90a001ae70a9caa95-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "ALL"
                    args = ["'string'"]
                    
            class LOWer(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:LOWer
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "LOWer"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:LOWer:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f170628c1afb430e.htm#ID_ce8edc7ffa896f2c0a00206a00e12ff4-d2a79ea4fa89698e0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class FEED(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:LOWer:FEED
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/736e608ceccb45ab.htm#ID_0a02e1e6fa8958970a00206a01102a1b-58c77064fa8952ea0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "FEED"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class SHIFt(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:LOWer:SHIFt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ebe098175c6f4345.htm#ID_42c4bc43fa8960280a00206a0190c6a5-473dcd87fa895a7b0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "SHIFt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:LIMit:LOWer:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b94fb57fc16a4021.htm#ID_5e22d895fa89679a0a00206a0189df49-6c41edc1fa8961fd0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class RDOMain(SCPINode):
                """
                CALCulate:LIMit:RDOMain
                
                Arguments: 
                """
                _cmd = "RDOMain"
                args = [""]
                
                class COMPlex(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:RDOMain:COMPlex
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/238f51657b44402d.htm#ID_1bfa6dc5fa89770c0a00206a011e3406-6dd1f87bfa89715e0a00206a01a6673d-en-US>`_
                    
                    Arguments: S, SINV, Y, YREL, Z, ZREL
                    """
                    _cmd = "COMPlex"
                    args = ["S", "SINV", "Y", "YREL", "Z", "ZREL"]
                    
                class FORMat(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:RDOMain:FORMat
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6cac5c97886d4899.htm#ID_d0fa1e97fa897ecc0a00206a00a410e7-fc19fdddfa8978f00a00206a01a6673d-en-US>`_
                    
                    Arguments: C, COMPlex, GDELay, IMAGinary, L, MAGNitude, PHASe, REAL, SWR
                    """
                    _cmd = "FORMat"
                    args = ["C", "COMPlex", "GDELay", "IMAGinary", "L", "MAGNitude", "PHASe", "REAL", "SWR"]
                    
                class SPACing(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:RDOMain:SPACing
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/fbdd7a3d75284494.htm#ID_d10f581ffa89866d0a00206a01cdc12f-072c5dfcfa8980c00a00206a01a6673d-en-US>`_
                    
                    Arguments: DB, LINear, LOGarithmic, SIC
                    """
                    _cmd = "SPACing"
                    args = ["DB", "LINear", "LOGarithmic", "SIC"]
                    
            class SEGMent(SCPINodeN):
                """
                CALCulate:LIMit:SEGMent
                
                Arguments: 
                """
                _cmd = "SEGMent"
                args = [""]
                
                class AMPLitude(SCPINode):
                    """
                    CALCulate:LIMit:SEGMent:AMPLitude
                    
                    Arguments: 
                    """
                    _cmd = "AMPLitude"
                    args = [""]
                    
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:SEGMent:AMPLitude:STARt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/11b0747d8e944b4b.htm#ID_79d6b03cfa898f560a00206a0037e778-eaa1c80cfa89898a0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STARt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:SEGMent:AMPLitude:STOP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/11b0747d8e944b4b.htm#ID_82e40f82fa8996d80a00206a019caca5-517eee2dfa89913b0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STOP"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class COUNt(SCPINode, SCPIQuery):
                    """
                    `CALCulate:LIMit:SEGMent:COUNt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f00309e159e4411c.htm#ID_a4781db3fa899eb80a00206a004cbe94-9a955102fa8998cc0a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "COUNt"
                    args = [""]
                    
                class STIMulus(SCPINode):
                    """
                    CALCulate:LIMit:SEGMent:STIMulus
                    
                    Arguments: 
                    """
                    _cmd = "STIMulus"
                    args = [""]
                    
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:SEGMent:STIMulus:STARt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d668e7d16044438d.htm#ID_d1275cb9fa89a6590a00206a01db09d6-4a3c58bdfa89a09c0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STARt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:LIMit:SEGMent:STIMulus:STOP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d668e7d16044438d.htm#ID_f98528d0fa89adbb0a00206a011164e6-65241391fa89a83d0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STOP"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:SEGMent:TYPE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2b4cba8b57db4862.htm#ID_b6e64935fa89b55c0a00206a00c5b92a-00be6b1ffa89afa00a00206a01a6673d-en-US>`_
                    
                    Arguments: LMAX, LMIN, OFF
                    """
                    _cmd = "TYPE"
                    args = ["LMAX", "LMIN", "OFF"]
                    
            class SOUNd(SCPINode, SCPIBool):
                """
                CALCulate:LIMit:SOUNd
                
                Arguments: 1, OFF, ON
                """
                _cmd = "SOUNd"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:LIMit:SOUNd:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/eecfbfbc00724725.htm#ID_8cff667afa89bd0d0a00206a002b9bb9-c7083814fa89b7310a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:LIMit:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/41d4ae0c38fe49c4.htm#ID_a2351470fa89c49f0a00206a003ef800-63a4586cfa89bef20a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
                class AREA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:STATe:AREA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9d9e42e32fcf45e6.htm#ID_e4bbdf5091dad73d0a00206a015f6524-9e0d80eb91dacdd70a00206a00e9ecac-en-US>`_
                    
                    Arguments: LEFT, MID, RIGHt
                    """
                    _cmd = "AREA"
                    args = ["LEFT", "MID", "RIGHt"]
                    
            class TTLout(SCPINodeN, SCPIBool):
                """
                CALCulate:LIMit:TTLout
                
                Arguments: 1, OFF, ON
                """
                _cmd = "TTLout"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:LIMit:TTLout:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8c5a247317814d57.htm#ID_cbcffdacfa89ccbd0a00206a00b40a25-4afe7823fa89c6930a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class UPPer(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:LIMit:UPPer
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "UPPer"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:LIMit:UPPer:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f170628c1afb430e.htm#ID_bc7a4fc8fa89ebbe0a00206a0189234d-9a27fa013c961f1f0a00201901e2ea6c-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class FEED(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:UPPer:FEED
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/736e608ceccb45ab.htm#ID_120c8703fa89d46d0a00206a0192176f-bb730b26fa89cea10a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "FEED"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class SHIFt(SCPINode, SCPISet):
                    """
                    `CALCulate:LIMit:UPPer:SHIFt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ebe098175c6f4345.htm#ID_4049dd9cfa89dbff0a00206a01134819-274d8fa3fa89d6610a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "SHIFt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:LIMit:UPPer:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b94fb57fc16a4021.htm#ID_63005ebdfa89e3ee0a00206a016ea114-723fb281fa89ddf30a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
        class MARKer(SCPINodeN, SCPIBool):
            """
            CALCulate:MARKer
            
            Arguments: 1, OFF, ON
            """
            _cmd = "MARKer"
            args = ["1", "OFF", "ON"]
            
            class AOFF(SCPINode, SCPISet):
                """
                `CALCulate:MARKer:AOFF
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/fa000f93fd4f4c5b.htm#ID_c984dcecfa89f38e0a00206a00d27a1c-ca2a1fc1fa89edb20a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "AOFF"
                args = [""]
                
            class BWIDth(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:BWIDth
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8db4f4a0d76a456e.htm#ID_c87ace40fa89fb3f0a00206a01891879-b1201654fa89f5820a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "BWIDth"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class COUPled(SCPINode, SCPIBool):
                """
                CALCulate:MARKer:COUPled
                
                Arguments: 1, OFF, ON
                """
                _cmd = "COUPled"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:MARKer:COUPled:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1bd62bd7692f4e41.htm#ID_3afb171ffa8a030f0a00206a00a6f15a-8e7bcef9fa89fd230a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class DEFault(SCPINode):
                """
                CALCulate:MARKer:DEFault
                
                Arguments: 
                """
                _cmd = "DEFault"
                args = [""]
                
                class FORMat(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:DEFault:FORMat
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f47b7220e9a24599.htm#ID_a1916f36353430b80a001ae733a2d25d-cf535f9435342f120a001ae72ac1dc63-en-US>`_
                    
                    Arguments: ADMittance, COMPlex, DEFault, GDELay, IMAGinary, IMPedance, LINPhase, LOGPhase, MDB, MDPHase, MIMPedance, MLINear, MLOGarithmic, MLPHase, PHASe, POLar, REAL, SWR
                    """
                    _cmd = "FORMat"
                    args = ["ADMittance", "COMPlex", "DEFault", "GDELay", "IMAGinary", "IMPedance", "LINPhase", "LOGPhase", "MDB", "MDPHase", "MIMPedance", "MLINear", "MLOGarithmic", "MLPHase", "PHASe", "POLar", "REAL", "SWR"]
                    
            class DELTa(SCPINode, SCPIBool):
                """
                CALCulate:MARKer:DELTa
                
                Arguments: 1, OFF, ON
                """
                _cmd = "DELTa"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:MARKer:DELTa:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9a00eb7a33d84165.htm#ID_2ac31b0bfa8a0aa00a00206a014d68e5-7bbe3cfbfa8a04f30a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class FORMat(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:FORMat
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4c7af5ff6777435b.htm#ID_0c7f97fada30383f0a001ae704ff0606-a607c8b9fa8a0c750a00206a01a6673d-en-US>`_
                
                Arguments: ADMittance, COMPlex, DEFault, GDELay, IMAGinary, IMPedance, LINPhase, LOGPhase, MDB, MDPHase, MIMPedance, MLINear, MLOGarithmic, MLPHase, PHASe, POLar, REAL, SWR
                """
                _cmd = "FORMat"
                args = ["ADMittance", "COMPlex", "DEFault", "GDELay", "IMAGinary", "IMPedance", "LINPhase", "LOGPhase", "MDB", "MDPHase", "MIMPedance", "MLINear", "MLOGarithmic", "MLPHase", "PHASe", "POLar", "REAL", "SWR"]
                
            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MARKer:FUNCtion
                
                Arguments: BFILter, LPEak, LTARget, MAXimum, MINimum, MMAXimum, MMINimum, NPEak, RPEak, RTARget, TARGet
                """
                _cmd = "FUNCtion"
                args = ["BFILter", "LPEak", "LTARget", "MAXimum", "MINimum", "MMAXimum", "MMINimum", "NPEak", "RPEak", "RTARget", "TARGet"]
                
                class BWIDth(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:BWIDth
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/18d64e401a3c4d78.htm#ID_e192fb1bfa8a28e60a00206a0079aa26-15468232fa8a23290a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "BWIDth"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                    class GMCenter(SCPINode, SCPIBool):
                        """
                        `CALCulate:MARKer:FUNCtion:BWIDth:GMCenter
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9ea2897cc2074b65.htm#ID_09cba1695d2e9a7e0a001ae73dea0c2a-40db97d65d2e98f80a001ae75392d2c4-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "GMCenter"
                        args = ["1", "OFF", "ON"]
                        
                    class MODE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:MARKer:FUNCtion:BWIDth:MODE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0a26f3b8139d4bb4.htm#ID_791788fefa8a30c60a00206a00649e10-787c5f72fa8a2abb0a00206a01a6673d-en-US>`_
                        
                        Arguments: BPABsolute, BPASs, BPRMarker, BSABsolute, BSRMarker, BSTop, NONE
                        """
                        _cmd = "MODE"
                        args = ["BPABsolute", "BPASs", "BPRMarker", "BSABsolute", "BSRMarker", "BSTop", "NONE"]
                        
                class CENTer(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:CENTer
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8c94020d00ed4c26.htm#ID_365edbb4fa8a38960a00206a00bd8439-2a58127bfa8a32ba0a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "CENTer"
                    args = [""]
                    
                class DELTa(SCPINode):
                    """
                    CALCulate:MARKer:FUNCtion:DELTa
                    
                    Arguments: 
                    """
                    _cmd = "DELTa"
                    args = [""]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `CALCulate:MARKer:FUNCtion:DELTa:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6b65d72689764580.htm#ID_1d43c878fa8a40660a00206a011298cf-abb3447cfa8a3a8a0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class DOMain(SCPINode):
                    """
                    CALCulate:MARKer:FUNCtion:DOMain
                    
                    Arguments: 
                    """
                    _cmd = "DOMain"
                    args = [""]
                    
                    class USER(SCPINode, SCPIQuery, SCPISet):
                        """
                        CALCulate:MARKer:FUNCtion:DOMain:USER
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "USER"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                        class RANGe(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:MARKer:FUNCtion:DOMain:USER:RANGe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2af2a460e1634e13.htm#ID_ec748740a1e91ec20a001ae73c718e26-cff20544a1e91da90a001ae70a9caa95-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "RANGe"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class SHOW(SCPINode, SCPIBool):
                            """
                            `CALCulate:MARKer:FUNCtion:DOMain:USER:SHOW
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b996f7d9a11b400a.htm#ID_0bf0909ffa8a4fe60a00206a01917992-7f696627fa8a49dc0a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "SHOW"
                            args = ["1", "OFF", "ON"]
                            
                        class STARt(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:MARKer:FUNCtion:DOMain:USER:STARt
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6b09f447b71d417a.htm#ID_a5f79d01fa8a57e50a00206a002de6dc-52538baffa8a51ea0a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "STARt"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class STOP(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:MARKer:FUNCtion:DOMain:USER:STOP
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6b09f447b71d417a.htm#ID_687ae9d6fa8a60030a00206a007c1291-2f4051c6fa8a59ca0a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "STOP"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                class EXECute(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:EXECute
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/600b76c1f17b4625.htm#ID_0f48fc24fa8a67f30a00206a017b7ffd-4761b5f8fa8a61e80a00206a01a6673d-en-US>`_
                    
                    Arguments: BFILter, LPEak, LTARget, MAXimum, MINimum, MMAXimum, MMINimum, NPEak, RPEak, RTARget, TARGet
                    """
                    _cmd = "EXECute"
                    args = ["BFILter", "LPEak", "LTARget", "MAXimum", "MINimum", "MMAXimum", "MMINimum", "NPEak", "RPEak", "RTARget", "TARGet"]
                    
                class RESult(SCPINode, SCPIQuery):
                    """
                    `CALCulate:MARKer:FUNCtion:RESult
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c4a647dafdef46ee.htm#ID_ca4abd32fa8a6f840a00206a01da7da1-6cf5cdc7fa8a69c70a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "RESult"
                    args = [""]
                    
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:SELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c95147813aef4387.htm#ID_28ad0b13fa8a8e860a00206a002e5875-64e78ee7fa8a884c0a00206a01a6673d-en-US>`_
                    
                    Arguments: BFILter, LPEak, LTARget, MAXimum, MINimum, MMAXimum, MMINimum, NPEak, RPEak, RTARget, TARGet
                    """
                    _cmd = "SELect"
                    args = ["BFILter", "LPEak", "LTARget", "MAXimum", "MINimum", "MMAXimum", "MMINimum", "NPEak", "RPEak", "RTARget", "TARGet"]
                    
                class SPAN(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:SPAN
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d16c29d1400f4678.htm#ID_8d68f92e6c02ab810a00206a01c2603f-22bc3ca36c02a4da0a00206a01eade93-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "SPAN"
                    args = [""]
                    
                class STARt(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:STARt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ceab94aa505047d1.htm#ID_c6f90737fa8a77350a00206a00929601-35edf04bfa8a71780a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "STARt"
                    args = [""]
                    
                class STOP(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:STOP
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ceab94aa505047d1.htm#ID_c5b678bdfa8a7ed60a00206a007ab819-384b0a87fa8a790a0a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "STOP"
                    args = [""]
                    
                class TARGet(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:FUNCtion:TARGet
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7c2d30605ca841ae.htm#ID_bc960c67fa8a86770a00206a0083f28b-98cf2789fa8a80ab0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "TARGet"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class MAXimum(SCPINode, SCPISet):
                """
                `CALCulate:MARKer:MAXimum
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dd071845c23d417a.htm#ID_8c34c922fa8a983a0a00206a00c82880-06d37e32fa8a91160a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "MAXimum"
                args = [""]
                
            class MINimum(SCPINode, SCPISet):
                """
                `CALCulate:MARKer:MINimum
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dd071845c23d417a.htm#ID_4ad27e65fa8aa1420a00206a0153b85a-e85401f8fa8a9aba0a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "MINimum"
                args = [""]
                
            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:MODE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4010b689c6bf4ec7.htm#ID_b49e503bfa8aa9af0a00206a01c8eac3-1a6dc12efa8aa3a40a00206a01a6673d-en-US>`_
                
                Arguments: CONTinuous, DISCrete
                """
                _cmd = "MODE"
                args = ["CONTinuous", "DISCrete"]
                
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:NAME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d956e2c3002e4abd.htm#ID_a680fdc9fa8ab2980a00206a000a65ae-163ea644fa8aaba30a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "NAME"
                args = ["'string'"]
                
            class REFerence(SCPINode, SCPIBool):
                """
                CALCulate:MARKer:REFerence
                
                Arguments: 1, OFF, ON
                """
                _cmd = "REFerence"
                args = ["1", "OFF", "ON"]
                
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:MODE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/44bfec6a89d24ef8.htm#ID_603a1492fa8abac50a00206a0069c536-856117a3fa8ab5180a00206a01a6673d-en-US>`_
                    
                    Arguments: CONTinuous, DISCrete
                    """
                    _cmd = "MODE"
                    args = ["CONTinuous", "DISCrete"]
                    
                class NAME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:NAME
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/87ac5dca438a4cdd.htm#ID_999919fdfa8ac2950a00206a01882570-c28c1b05fa8abc9a0a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "NAME"
                    args = ["'string'"]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:MARKer:REFerence:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6ea0ed2e1ddf4f74.htm#ID_38b890f5fa8b86330a00206a01954afc-5cd7d92dfa8b80760a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:TYPE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7c0f3d498f264e9e.htm#ID_20c235fafa8b6eb30a00206a01dede11-49a0afa4fa8b685a0a00206a01a6673d-en-US>`_
                    
                    Arguments: FIXed, NORMal
                    """
                    _cmd = "TYPE"
                    args = ["FIXed", "NORMal"]
                    
                class X(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:REFerence:X
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/57b141f2e2c44fb9.htm#ID_17e585b9fa8b76b20a00206a002d73ab-c4bf51adfa8b70980a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "X"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class Y(SCPINode, SCPIQuery):
                    """
                    `CALCulate:MARKer:REFerence:Y
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/90520d3afddd4fde.htm#ID_6e8f4665fa8b7e630a00206a01ed19b0-7b490ccffa8b78b60a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "Y"
                    args = [""]
                    
            class SEARch(SCPINode, SCPISet):
                """
                CALCulate:MARKer:SEARch
                
                Arguments: 
                """
                _cmd = "SEARch"
                args = [""]
                
                class BFILter(SCPINode):
                    """
                    CALCulate:MARKer:SEARch:BFILter
                    
                    Arguments: 
                    """
                    _cmd = "BFILter"
                    args = [""]
                    
                    class RESult(SCPINode, SCPIBool):
                        """
                        CALCulate:MARKer:SEARch:BFILter:RESult
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "RESult"
                        args = ["1", "OFF", "ON"]
                        
                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:MARKer:SEARch:BFILter:RESult:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f2d891a03a1d49f9.htm#ID_b0cb39b7fa8b8e410a00206a00d7eda6-57e9f681fa8b88080a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                            class AREA(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:MARKer:SEARch:BFILter:RESult:STATe:AREA
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e2feccae7432448d.htm#ID_3d27cc9c91db00ce0a00206a01798cde-8853842091daf8230a00206a00e9ecac-en-US>`_
                                
                                Arguments: LEFT, MID, RIGHt
                                """
                                _cmd = "AREA"
                                args = ["LEFT", "MID", "RIGHt"]
                                
                class FORMat(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:FORMat
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d201a42d7ccc45ed.htm#ID_365c6ea35de572610a00201900016e84-655449015de571290a0020190152315a-en-US>`_
                    
                    Arguments: DEFault, IMAGinary, MLINear, MLOGarithmic, PHASe, REAL, SWR, UPHase
                    """
                    _cmd = "FORMat"
                    args = ["DEFault", "IMAGinary", "MLINear", "MLOGarithmic", "PHASe", "REAL", "SWR", "UPHase"]
                    
                class IMMediate(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:IMMediate
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4a78723c9cff4eef.htm#ID_8220efeafa8bb61c0a00206a002cc9cf-50585b86fa8baff20a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "IMMediate"
                    args = [""]
                    
                class LEFT(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:LEFT
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cdfa7b0040b0418c.htm#ID_8278f555fa8b96210a00206a0146cca2-c96c28e0fa8b90160a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "LEFT"
                    args = [""]
                    
                class NEXT(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:NEXT
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cdfa7b0040b0418c.htm#ID_3ef4139bfa8b9de10a00206a0020e6d6-55733c3dfa8b98150a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "NEXT"
                    args = [""]
                    
                class RIGHt(SCPINode, SCPISet):
                    """
                    `CALCulate:MARKer:SEARch:RIGHt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cdfa7b0040b0418c.htm#ID_f8f11fcbfa8ba61f0a00206a00095eea-c2ff6c7afa8ba0330a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "RIGHt"
                    args = [""]
                    
                class TRACking(SCPINode, SCPIBool):
                    """
                    `CALCulate:MARKer:SEARch:TRACking
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/50067f6406044da9.htm#ID_47207a16fa8bae0e0a00206a008d852a-04f0dca6fa8ba8220a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "TRACking"
                    args = ["1", "OFF", "ON"]
                    
            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:MARKer:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d0472df6b3cb40c9.htm#ID_e745149dfa8be1340a00206a01305b71-b428f5aefa8bdb380a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
                class AREA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MARKer:STATe:AREA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/59688d861c344dbc.htm#ID_4bccbbec91db0bda0a00206a01d2f8b1-2b62471a91db04390a00206a00e9ecac-en-US>`_
                    
                    Arguments: LEFT, MID, RIGHt
                    """
                    _cmd = "AREA"
                    args = ["LEFT", "MID", "RIGHt"]
                    
            class TARGet(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:TARGet
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8f93a1eedbcb4346.htm#ID_6773dc66fa8bbe890a00206a01e71f6d-ee358b16fa8bb7f10a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "TARGet"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class TYPE(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:TYPE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8740dafec1944a52.htm#ID_6ec07d71fa8bc8aa0a00206a01cd9de5-4689d12efa8bc0ea0a00206a01a6673d-en-US>`_
                
                Arguments: FIXed, NORMal
                """
                _cmd = "TYPE"
                args = ["FIXed", "NORMal"]
                
            class X(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MARKer:X
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4ef3e6895bcf42b7.htm#ID_2358db0ffa8bd1840a00206a01e12053-393c91dcfa8bcb690a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "X"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class Y(SCPINode, SCPIQuery):
                """
                `CALCulate:MARKer:Y
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8d8c242cdd7e4572.htm#ID_68d57989fa8bd9540a00206a0034e41b-a588c4c5fa8bd3590a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "Y"
                args = [""]
                
        class MATH(SCPINode, SCPIQuery, SCPISet):
            """
            CALCulate:MATH
            
            Arguments: (expression)
            """
            _cmd = "MATH"
            args = ["(expression)"]
            
            class EXPRession(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:MATH:EXPRession
                
                Arguments: (expression)
                """
                _cmd = "EXPRession"
                args = ["(expression)"]
                
                class DEFine(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MATH:EXPRession:DEFine
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/49b93df4d2974c24.htm#ID_8520d66dfa8c11b90a00206a002e410f-5fdc9322fa8c0c0c0a00206a01a6673d-en-US>`_
                    
                    Arguments: (expression)
                    """
                    _cmd = "DEFine"
                    args = ["(expression)"]
                    
                class SDEFine(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:MATH:EXPRession:SDEFine
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7d726687c3514fa3.htm#ID_a2f75c6cfa8c0a370a00206a0145ed97-d61bd978fa8c049a0a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "SDEFine"
                    args = ["'string'"]
                    
            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:MATH:FUNCtion
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ffdc5ec43e98489c.htm#ID_39a94accfa8be8b50a00206a00eb9289-d8e4b798fa8be3080a00206a01a6673d-en-US>`_
                
                Arguments: ADD, DIVide, MULTiply, NORMal, SUBTract
                """
                _cmd = "FUNCtion"
                args = ["ADD", "DIVide", "MULTiply", "NORMal", "SUBTract"]
                
            class MEMorize(SCPINode, SCPISet):
                """
                `CALCulate:MATH:MEMorize
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1bc091561bf04c5d.htm#ID_8c53fd1afa8bf20c0a00206a01fcb1ce-8e069e7efa8beb260a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "MEMorize"
                args = [""]
                
            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:MATH:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5826421b58a046ed.htm#ID_68bf5aa0fa8bfae60a00206a01d8cc25-038f9478fa8bf43e0a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
            class WUNit(SCPINode, SCPIBool):
                """
                CALCulate:MATH:WUNit
                
                Arguments: 1, OFF, ON
                """
                _cmd = "WUNit"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:MATH:WUNit:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9628726622464f1c.htm#ID_020fd1e7fa8c02c50a00206a01046c97-6a5ac2ccfa8bfce90a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
        class PARameter(SCPINode):
            """
            CALCulate:PARameter
            
            Arguments: 
            """
            _cmd = "PARameter"
            args = [""]
            
            class CATalog(SCPINode, SCPIQuery):
                """
                `CALCulate:PARameter:CATalog
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2ce049f1af684d21.htm#ID_6d0f03abfa8c193b0a00206a003b5f50-8685a90cfa8c13bd0a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "CATalog"
                args = [""]
                
                class SENDed(SCPINode, SCPIQuery):
                    """
                    `CALCulate:PARameter:CATalog:SENDed
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4aaff69b21544d46.htm#ID_72b3d670842dc4af0a00201900a9cfc5-ae203438842dc3380a00201901936165-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "SENDed"
                    args = [""]
                    
            class DEFine(SCPINode, SCPISet):
                """
                `CALCulate:PARameter:DEFine
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/85c286e91d1f45c1.htm#ID_c26a23a6fa8c20bd0a00206a01ef3d1b-d5d71622fa8c1b100a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "DEFine"
                args = ["'string'"]
                
                class SGRoup(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:PARameter:DEFine:SGRoup
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/78a4125ac51a435a.htm#ID_119cf020fa8c283f0a00206a00a5b7f1-6f48d8a2fa8c22920a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "SGRoup"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class DELete(SCPINode, SCPISet):
                """
                `CALCulate:PARameter:DELete
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0763f74d0a2d4d61.htm#ID_8f70dcdefa8c2fe00a00206a003b801c-ee007debfa8c2a330a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "DELete"
                args = ["'string'"]
                
                class ALL(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e75933.htm#ID_aaf85c1de1568dfc0a00206a01ec5604-135cad8de15685420a00206a00796295-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "ALL"
                    args = [""]
                    
                class CALL(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:CALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8d937272d97244fb.htm#ID_8d9ff76be156a6a50a00206a01182ba4-6f8706dce1569d5e0a00206a00796295-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "CALL"
                    args = [""]
                    
                class CMEMory(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:CMEMory
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cc3d9af74e704b5c.htm#ID_a75b324c4b6a080e0a001ae706c6f2b3-ded67b324b6a04740a001ae708cb241d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "CMEMory"
                    args = [""]
                    
                class MEMory(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:MEMory
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4613fe70603c4f9d.htm#ID_96a98c814b6a0ce00a001ae76e6a3196-75f503b24b6a09d30a001ae708cb241d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "MEMory"
                    args = [""]
                    
                class SGRoup(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:DELete:SGRoup
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bc5ac4b592724e7a.htm#ID_f2764fe1fa8c37520a00206a01e48f49-65ba2f61fa8c31b50a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "SGRoup"
                    args = [""]
                    
            class MEASure(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:PARameter:MEASure
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/10abfaa35dcf40f3.htm#ID_b2e7e077fa8c3ef30a00206a00c865a1-07a6d833fa8c39460a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "MEASure"
                args = ["'string'"]
                
                class SENDed(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:PARameter:MEASure:SENDed
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c7009e9c24ab41ca.htm#ID_e36c8c14842dcc210a00201900ce962e-6d066a16842dcac90a00201901936165-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "SENDed"
                    args = ["'string'"]
                    
            class SDEFine(SCPINode, SCPISet):
                """
                `CALCulate:PARameter:SDEFine
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e75d49e2a14541c5.htm#ID_e2a5b54afa8c4dd80a00206a00d8bd4a-b73200d6fa8c482b0a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "SDEFine"
                args = ["'string'"]
                
                class SENDed(SCPINode, SCPISet):
                    """
                    `CALCulate:PARameter:SDEFine:SENDed
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/87172ee6d3f0486d.htm#ID_22046707842dcee00a002019009c3503-c048e5e3842dcd5a0a00201901936165-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "SENDed"
                    args = ["'string'"]
                    
            class SELect(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:PARameter:SELect
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3c03effa6de64ee5.htm#ID_fa5a7dabfa8c555a0a00206a00a4a885-9edb1c2efa8c4fac0a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "SELect"
                args = ["'string'"]
                
        class PHOLd(SCPINode, SCPIQuery, SCPISet):
            """
            `CALCulate:PHOLd
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7be6f52751ea485d.htm#ID_98d0d154fa8c5cfb0a00206a01cc0c79-20de90e3fa8c573e0a00206a01a6673d-en-US>`_
            
            Arguments: MAX, MIN, OFF
            """
            _cmd = "PHOLd"
            args = ["MAX", "MIN", "OFF"]
            
        class RIPPle(SCPINode):
            """
            CALCulate:RIPPle
            
            Arguments: 
            """
            _cmd = "RIPPle"
            args = [""]
            
            class CLEar(SCPINode, SCPISet):
                """
                `CALCulate:RIPPle:CLEar
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bc102c309ca64801.htm#ID_30c2583ee2b2b2890a00201901f4a3cf-911a2616e2b2b1600a002019017b841c-en-US>`_
                
                Arguments: 
                """
                _cmd = "CLEar"
                args = [""]
                
            class CONTrol(SCPINode):
                """
                CALCulate:RIPPle:CONTrol
                
                Arguments: 
                """
                _cmd = "CONTrol"
                args = [""]
                
                class DOMain(SCPINode, SCPISet):
                    """
                    `CALCulate:RIPPle:CONTrol:DOMain
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/efa433eb0a4a488d.htm#ID_6271dbebfa8c648c0a00206a01bc324d-fe0c5318fa8c5edf0a00206a01a6673d-en-US>`_
                    
                    Arguments: FLIN, FLOG, FSEG, FSINgle, PLIN, PLOG, PSINgle, TLIN, TLOG
                    """
                    _cmd = "DOMain"
                    args = ["FLIN", "FLOG", "FSEG", "FSINgle", "PLIN", "PLOG", "PSINgle", "TLIN", "TLOG"]
                    
            class DATA(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:RIPPle:DATA
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/003f16e0af9744b9.htm#ID_bd72ae33fa8c6bfe0a00206a0156adc6-dec22044fa8c66700a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "DATA"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class DELete(SCPINode):
                """
                CALCulate:RIPPle:DELete
                
                Arguments: 
                """
                _cmd = "DELete"
                args = [""]
                
                class ALL(SCPINode, SCPISet):
                    """
                    `CALCulate:RIPPle:DELete:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/80e7731362314ea3.htm#ID_cb829192fa8c73710a00206a00e729bd-16eb12ddfa8c6de30a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "ALL"
                    args = [""]
                    
            class DISPlay(SCPINode, SCPIBool):
                """
                CALCulate:RIPPle:DISPlay
                
                Arguments: 1, OFF, ON
                """
                _cmd = "DISPlay"
                args = ["1", "OFF", "ON"]
                
                class RESult(SCPINode):
                    """
                    CALCulate:RIPPle:DISPlay:RESult
                    
                    Arguments: 
                    """
                    _cmd = "RESult"
                    args = [""]
                    
                    class ALL(SCPINode, SCPIBool):
                        """
                        CALCulate:RIPPle:DISPlay:RESult:ALL
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "ALL"
                        args = ["1", "OFF", "ON"]
                        
                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:RIPPle:DISPlay:RESult:ALL:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9252124bcddc41e8.htm#ID_283b9afd5d2eb3c30a001ae73e7db882-361816a15d2eb29a0a001ae75392d2c4-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:RIPPle:DISPlay:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/af30ef097a4240bb.htm#ID_eec53853fa8c7af20a00206a017b8a53-82ea5f14fa8c75360a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class FAIL(SCPINode, SCPIQuery):
                """
                `CALCulate:RIPPle:FAIL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a6f184c34daa43c5.htm#ID_2d1b4441fa8c82840a00206a01c73f6d-bcd238bdfa8c7cc70a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "FAIL"
                args = [""]
                
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:RIPPle:FAIL:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3ff9874b75fd4b77.htm#ID_982687eba1e9377a0a001ae71d33ac9e-7cc4d3dda1e936130a001ae70a9caa95-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "ALL"
                    args = ["'string'"]
                    
            class RDOMain(SCPINode):
                """
                CALCulate:RIPPle:RDOMain
                
                Arguments: 
                """
                _cmd = "RDOMain"
                args = [""]
                
                class FORMat(SCPINode, SCPISet):
                    """
                    `CALCulate:RIPPle:RDOMain:FORMat
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/96a8405a7acb4768.htm#ID_c02c1b65fa8c89f60a00206a00ef0219-80cbde3efa8c84590a00206a01a6673d-en-US>`_
                    
                    Arguments: C, COMPlex, GDELay, IMAGinary, L, MAGNitude, PHASe, REAL, SWR
                    """
                    _cmd = "FORMat"
                    args = ["C", "COMPlex", "GDELay", "IMAGinary", "L", "MAGNitude", "PHASe", "REAL", "SWR"]
                    
            class SEGMent(SCPINodeN, SCPIBool):
                """
                CALCulate:RIPPle:SEGMent
                
                Arguments: 1, OFF, ON
                """
                _cmd = "SEGMent"
                args = ["1", "OFF", "ON"]
                
                class COUNt(SCPINode, SCPIQuery):
                    """
                    `CALCulate:RIPPle:SEGMent:COUNt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f6dd927483bd4b0b.htm#ID_157eedbefa8c91680a00206a01a10a29-76eb58c0fa8c8bda0a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "COUNt"
                    args = [""]
                    
                class LIMit(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:RIPPle:SEGMent:LIMit
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b53e47cd6ee84c63.htm#ID_c0af3f18fa8c98ea0a00206a0153bc80-411a2a59fa8c934d0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "LIMit"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class RESult(SCPINode, SCPIQuery):
                    """
                    `CALCulate:RIPPle:SEGMent:RESult
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/588bd177edf54661.htm#ID_5ae347ddfa8ca08b0a00206a00280543-d97d0bb0fa8c9acf0a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "RESult"
                    args = [""]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:RIPPle:SEGMent:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/56affa087259447b.htm#ID_a7b1806cfa8cb77e0a00206a017e3363-e5617d47fa8cb1c10a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
                class STIMulus(SCPINode):
                    """
                    CALCulate:RIPPle:SEGMent:STIMulus
                    
                    Arguments: 
                    """
                    _cmd = "STIMulus"
                    args = [""]
                    
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:RIPPle:SEGMent:STIMulus:STARt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e14be574123e48c9.htm#ID_a5c3ac7ffa8ca83c0a00206a017a8448-adda4ba4fa8ca2600a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STARt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:RIPPle:SEGMent:STIMulus:STOP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e14be574123e48c9.htm#ID_10f947ddfa8cafed0a00206a0105be95-4d344ccefa8caa200a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STOP"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
            class SOUNd(SCPINode, SCPIBool):
                """
                CALCulate:RIPPle:SOUNd
                
                Arguments: 1, OFF, ON
                """
                _cmd = "SOUNd"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:RIPPle:SOUNd:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3bf0aae076bc42bc.htm#ID_52557a3ffa8cbf100a00206a01806165-0b45785ffa8cb9530a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:RIPPle:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/fb623ebe7fb54f9b.htm#ID_f43adfc2fa8cc6820a00206a0172e6f5-e09bed1cfa8cc0e40a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
                class AREA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:RIPPle:STATe:AREA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4dc1b5a2821a4ae3.htm#ID_34fca1f991db93590a00206a01c30472-e3489bde91db8a700a00206a00e9ecac-en-US>`_
                    
                    Arguments: LEFT, MID, RIGHt
                    """
                    _cmd = "AREA"
                    args = ["LEFT", "MID", "RIGHt"]
                    
        class SMOothing(SCPINode, SCPIBool):
            """
            CALCulate:SMOothing
            
            Arguments: 1, OFF, ON
            """
            _cmd = "SMOothing"
            args = ["1", "OFF", "ON"]
            
            class APERture(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:SMOothing:APERture
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/529f93d8d2414119.htm#ID_0e07cb25fa8cce420a00206a0171f8ab-81a86b0efa8cc8660a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "APERture"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:SMOothing:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7811d02911894706.htm#ID_671d4593fa8cd6120a00206a0062fcac-cbb8b985fa8cd0270a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
        class STATistics(SCPINode, SCPIBool):
            """
            CALCulate:STATistics
            
            Arguments: 1, OFF, ON
            """
            _cmd = "STATistics"
            args = ["1", "OFF", "ON"]
            
            class DOMain(SCPINode):
                """
                CALCulate:STATistics:DOMain
                
                Arguments: 
                """
                _cmd = "DOMain"
                args = [""]
                
                class USER(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:STATistics:DOMain:USER
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a589efe7a4ea4cd2.htm#ID_9f963f50fa8cddb30a00206a005d21da-5aafc2dafa8cd7f70a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "USER"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                    class SHOW(SCPINode, SCPIBool):
                        """
                        `CALCulate:STATistics:DOMain:USER:SHOW
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7c04e1dc565f42fe.htm#ID_9b274ca7fa8ce5160a00206a01e534b5-014aff7efa8cdf880a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "SHOW"
                        args = ["1", "OFF", "ON"]
                        
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:DOMain:USER:STARt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8684a6f4edc14a42.htm#ID_feacdf2cfa8cec880a00206a00658f5d-d35f250cfa8ce6eb0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STARt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:DOMain:USER:STOP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8684a6f4edc14a42.htm#ID_9e04cc6bfa8cf4390a00206a016f509f-161fec51fa8cee9b0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STOP"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
            class EPDelay(SCPINode, SCPIBool):
                """
                CALCulate:STATistics:EPDelay
                
                Arguments: 1, OFF, ON
                """
                _cmd = "EPDelay"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:STATistics:EPDelay:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dd777ffb23ef4a85.htm#ID_ddeec772fa8cfbca0a00206a00768219-c4a76b8efa8cf61d0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class FORMat(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:STATistics:FORMat
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5af594af8b3d4ad3.htm#ID_9c03469b97e84b1c0a001ae7788a17fc-113e556897e849e40a001ae760f7f904-en-US>`_
                
                Arguments: ADMittance, IMPedance, ZVAB
                """
                _cmd = "FORMat"
                args = ["ADMittance", "IMPedance", "ZVAB"]
                
            class MMPTpeak(SCPINode, SCPIBool):
                """
                CALCulate:STATistics:MMPTpeak
                
                Arguments: 1, OFF, ON
                """
                _cmd = "MMPTpeak"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:STATistics:MMPTpeak:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dd777ffb23ef4a85.htm#ID_70eaa25efa8d034c0a00206a01b86abd-878c52c8fa8cfdbe0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class MSTDdev(SCPINode, SCPIBool):
                """
                CALCulate:STATistics:MSTDdev
                
                Arguments: 1, OFF, ON
                """
                _cmd = "MSTDdev"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:STATistics:MSTDdev:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dd777ffb23ef4a85.htm#ID_68163564fa8d0ace0a00206a006a35c4-9131f9e9fa8d05210a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class NLINear(SCPINode):
                """
                CALCulate:STATistics:NLINear
                
                Arguments: 
                """
                _cmd = "NLINear"
                args = [""]
                
                class COMP(SCPINode, SCPIBool):
                    """
                    CALCulate:STATistics:NLINear:COMP
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "COMP"
                    args = ["1", "OFF", "ON"]
                    
                    class LEVel(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:STATistics:NLINear:COMP:LEVel
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5d6c51b169d74dd1.htm#ID_c925aca6fa8d127f0a00206a00d4d7e8-4b0de918fa8d0cc20a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "LEVel"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class RESult(SCPINode, SCPIQuery):
                        """
                        `CALCulate:STATistics:NLINear:COMP:RESult
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d066840052e34270.htm#ID_877f774dfa8d1a010a00206a000c5799-9a74d1cdfa8d14730a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "RESult"
                        args = [""]
                        
                    class STATe(SCPINode, SCPIBool):
                        """
                        `CALCulate:STATistics:NLINear:COMP:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6bb074b56dab4d34.htm#ID_4bc3ff91fa8d21920a00206a00c0450c-b88e3168fa8d1bd50a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
            class RESult(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:STATistics:RESult
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/504c1240aaf84b48.htm#ID_9ad8a052fa8d29240a00206a018e8f49-cc55af54fa8d23670a00206a01a6673d-en-US>`_
                
                Arguments: ALL, ELENgth, FLATness, GAIN, MAX, MEAN, MIN, PDELay, PEAK2p, PTPeak, RMS, SLOPe, STDDev
                """
                _cmd = "RESult"
                args = ["ALL", "ELENgth", "FLATness", "GAIN", "MAX", "MEAN", "MIN", "PDELay", "PEAK2p", "PTPeak", "RMS", "SLOPe", "STDDev"]
                
            class RMS(SCPINode, SCPIBool):
                """
                CALCulate:STATistics:RMS
                
                Arguments: 1, OFF, ON
                """
                _cmd = "RMS"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:STATistics:RMS:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5ab4519994e14adf.htm#ID_3614abc9fa8d30860a00206a00131843-d95b7e56fa8d2af80a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class SFLatness(SCPINode, SCPIBool):
                """
                CALCulate:STATistics:SFLatness
                
                Arguments: 1, OFF, ON
                """
                _cmd = "SFLatness"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:STATistics:SFLatness:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5ab4519994e14adf.htm#ID_4120133afa8d38180a00206a01da59ef-a95d681dfa8d326b0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class STATe(SCPINode, SCPIBool):
                """
                `CALCulate:STATistics:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2f7b3f85defe4eb2.htm#ID_a5c56f11fa8d3f8a0a00206a001597a1-2c31185bfa8d39fc0a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
                class AREA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:STATistics:STATe:AREA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f48f70d27489445d.htm#ID_97e5221b91dbbcea0a00206a01e4bef3-0cc1fe9b91dbb5680a00206a00e9ecac-en-US>`_
                    
                    Arguments: LEFT, MID, RIGHt
                    """
                    _cmd = "AREA"
                    args = ["LEFT", "MID", "RIGHt"]
                    
        class TRANsform(SCPINode):
            """
            CALCulate:TRANsform
            
            Arguments: 
            """
            _cmd = "TRANsform"
            args = [""]
            
            class COMPlex(SCPINode, SCPIQuery, SCPISet):
                """
                `CALCulate:TRANsform:COMPlex
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0ddb2fb52f9647b1.htm#ID_6763dcf5fa8d4ebc0a00206a0172615e-fc0db3f8fa8d492f0a00206a01a6673d-en-US>`_
                
                Arguments: S, Y, Z
                """
                _cmd = "COMPlex"
                args = ["S", "Y", "Z"]
                
            class IMPedance(SCPINode):
                """
                CALCulate:TRANsform:IMPedance
                
                Arguments: 
                """
                _cmd = "IMPedance"
                args = [""]
                
                class RNORmal(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:IMPedance:RNORmal
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/14e821102ae54212.htm#ID_559024ddfa8d563e0a00206a008657c0-5f0233befa8d50a10a00206a01a6673d-en-US>`_
                    
                    Arguments: PWAVes, TWAVes
                    """
                    _cmd = "RNORmal"
                    args = ["PWAVes", "TWAVes"]
                    
            class TIME(SCPINode, SCPIQuery, SCPISet):
                """
                CALCulate:TRANsform:TIME
                
                Arguments: BPASs, LPASs
                """
                _cmd = "TIME"
                args = ["BPASs", "LPASs"]
                
                class CENTer(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:CENTer
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2d5ae32dc5f84be0.htm#ID_35afe348fa8d5dd00a00206a010edee7-6f4e2e2afa8d58320a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "CENTer"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class DCHebyshev(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:DCHebyshev
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bd1362285dd64cb0.htm#ID_4c77cbdefa8d668a0a00206a012d61e1-ecea3751fa8d60ed0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DCHebyshev"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class LPASs(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:LPASs
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f526f7ddf2884d92.htm#ID_170ddb9dfa8d6e0c0a00206a0187917f-377f1619fa8d686e0a00206a01a6673d-en-US>`_
                    
                    Arguments: KDFRequency, KFSTop, KSDFrequency
                    """
                    _cmd = "LPASs"
                    args = ["KDFRequency", "KFSTop", "KSDFrequency"]
                    
                    class DCSParam(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:TRANsform:TIME:LPASs:DCSParam
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/53ce9e90e07e4a51.htm#ID_4a46c475fa8d75cc0a00206a01e0e76f-bd956431fa8d6fe10a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "DCSParam"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                        class CONTinuous(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:TIME:LPASs:DCSParam:CONTinuous
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/eb8dd59636a74569.htm#ID_1c2005cafa8d7d4e0a00206a0174e6c4-98d7bc34fa8d77b10a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "CONTinuous"
                            args = ["1", "OFF", "ON"]
                            
                        class EXTRapolate(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:TIME:LPASs:DCSParam:EXTRapolate
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2dcd2a27ce744b66.htm#ID_675aa806fa8d84c00a00206a01e30f89-cfb2563cfa8d7f230a00206a01a6673d-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "EXTRapolate"
                            args = [""]
                            
                class LPFRequency(SCPINode, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:LPFRequency
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/27b41786fbb64c8c.htm#ID_e86cd025fa8d8c610a00206a00c7bfc0-581fc947fa8d86a50a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "LPFRequency"
                    args = [""]
                    
                class METHod(SCPINode, SCPIQuery, SCPISet):
                    """
                    CALCulate:TRANsform:TIME:METHod
                    
                    Arguments: CHIRp
                    """
                    _cmd = "METHod"
                    args = ["CHIRp"]
                    
                class RESolution(SCPINode):
                    """
                    CALCulate:TRANsform:TIME:RESolution
                    
                    Arguments: 
                    """
                    _cmd = "RESolution"
                    args = [""]
                    
                    class EFACtor(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CALCulate:TRANsform:TIME:RESolution:EFACtor
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/635fc83aab98475a.htm#ID_ed455756fa8d9b840a00206a01cbf0cc-c0ea7111fa8d95c80a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "EFACtor"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class SPAN(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:SPAN
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1e787fde60e7484a.htm#ID_e25bd601fa8da3060a00206a00fa1352-d688e1b8fa8d9d590a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "SPAN"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class STARt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:STARt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8ea0328127044ba9.htm#ID_6070a8edfa8daa980a00206a0032a239-a965258ffa8da4fa0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "STARt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `CALCulate:TRANsform:TIME:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/83fed5073fde47ee.htm#ID_024e8732fa8db2480a00206a01f94674-e8c96f45fa8dac7c0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
                class STIMulus(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:STIMulus
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0157afe1515d4140.htm#ID_2274ec00fa8db9ea0a00206a01a73a83-47ff8851fa8db41d0a00206a01a6673d-en-US>`_
                    
                    Arguments: IMPulse, STEP
                    """
                    _cmd = "STIMulus"
                    args = ["IMPulse", "STEP"]
                    
                class STOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:STOP
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4cd73ad6216545c4.htm#ID_c1eb53d4fa8dc18b0a00206a01c01ff2-c6268d0cfa8dbbce0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "STOP"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class TYPE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:TYPE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/baf83ae4b9fc4af4.htm#ID_883048c0fa8dd8200a00206a001376e6-4965ba92fa8dd2920a00206a01a6673d-en-US>`_
                    
                    Arguments: BPASs, LPASs
                    """
                    _cmd = "TYPE"
                    args = ["BPASs", "LPASs"]
                    
                class WINDow(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:WINDow
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/aac0f28b6e3041a6.htm#ID_08a5b679fa8dc92c0a00206a0171d219-eeb23c46fa8dc38e0a00206a01a6673d-en-US>`_
                    
                    Arguments: BOHMan, DCHebyshev, HAMMing, HANNing, RECT
                    """
                    _cmd = "WINDow"
                    args = ["BOHMan", "DCHebyshev", "HAMMing", "HANNing", "RECT"]
                    
                class XAXis(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CALCulate:TRANsform:TIME:XAXis
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2e1c9ec5c19b4efa.htm#ID_9a53dbaffa8dd0ae0a00206a01f538e4-a3eff330fa8dcb010a00206a01a6673d-en-US>`_
                    
                    Arguments: DISTance, TIME
                    """
                    _cmd = "XAXis"
                    args = ["DISTance", "TIME"]
                    
            class VNETworks(SCPINode):
                """
                CALCulate:TRANsform:VNETworks
                
                Arguments: 
                """
                _cmd = "VNETworks"
                args = [""]
                
                class BALanced(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:BALanced
                    
                    Arguments: 
                    """
                    _cmd = "BALanced"
                    args = [""]
                    
                    class DEEMbedding(SCPINodeN, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "DEEMbedding"
                        args = ["1", "OFF", "ON"]
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters
                            
                            Arguments: 
                            """
                            _cmd = "PARameters"
                            args = [""]
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6f0c9d49615148c7.htm#ID_dd8133a4fa8ddfc10a00206a01185633-3d70b06bfa8dda040a00206a01a6673d-en-US>`_
                                
                                Arguments: CSSC, CSSL, GSSG, GSSL, LSSC, LSSG, SCCS, SCLS, SCST, SGGS, SGLS, SGST, SLCS, SLGS, STSC, STSG
                                """
                                _cmd = "C"
                                args = ["CSSC", "CSSL", "GSSG", "GSSL", "LSSC", "LSSG", "SCCS", "SCLS", "SCST", "SGGS", "SGLS", "SGST", "SLCS", "SLGS", "STSC", "STSG"]
                                
                            class DATA(SCPINodeN, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:DATA
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/59ae1ad9a60e4c58.htm#ID_84293532842de3240a00201901e6e490-deedc1c0842de18d0a00201901936165-en-US>`_
                                
                                Arguments: FPORts, IPORts
                                """
                                _cmd = "DATA"
                                args = ["FPORts", "IPORts"]
                                
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:G
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3cb1c25a3e284cac.htm#ID_2b5d169b6f6624690a001ae7153f6596-6c03f7b66f6622f20a001ae727f5f310-en-US>`_
                                
                                Arguments: GSSG, GSSL, LSSG, SGGS, SGLS, SGST, SLGS, STSG
                                """
                                _cmd = "G"
                                args = ["GSSG", "GSSL", "LSSG", "SGGS", "SGLS", "SGST", "SLGS", "STSG"]
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1186eea832df4546.htm#ID_d84a0ce1fa8de7720a00206a00f5bb24-31cd32e7fa8de1a50a00206a01a6673d-en-US>`_
                                
                                Arguments: CSSL, GSSL, LSSC, LSSG, LSSL, SCLS, SGLS, SLCS, SLGS, SLLS, SLST, STSL
                                """
                                _cmd = "L"
                                args = ["CSSL", "GSSL", "LSSC", "LSSG", "LSSL", "SCLS", "SGLS", "SLCS", "SLGS", "SLLS", "SLST", "STSL"]
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f2ea1c1f6a88461f.htm#ID_a9c33f0dfa8def320a00206a00518f0d-c5a4cd8ffa8de9560a00206a01a6673d-en-US>`_
                                
                                Arguments: CSSC, CSSL, GSSL, LSSC, LSSG, LSSL, SCCS, SCLS, SCST, SGLS, SLCS, SLGS, SLLS, SLST, STSC, STSL
                                """
                                _cmd = "R"
                                args = ["CSSC", "CSSL", "GSSL", "LSSC", "LSSG", "LSSL", "SCCS", "SCLS", "SCST", "SGLS", "SLCS", "SLGS", "SLLS", "SLST", "STSC", "STSL"]
                                
                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4d9b6ee9116348ce.htm#ID_5172a9c4fa8dfe550a00206a01e07981-787e7537fa8df8980a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:DEEMbedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/12448e2e96f04df7.htm#ID_2a7d63bbfa8df6b40a00206a01d43e88-8940a4f2fa8df1160a00206a01a6673d-en-US>`_
                            
                            Arguments: CSSC, CSSL, FIMPort, GSSG, GSSL, LSSC, LSSG, LSSL, SCCS, SCLS, SCST, SGGS, SGLS, SGST, SLCS, SLGS, SLLS, SLST, STSC, STSG, STSL
                            """
                            _cmd = "TNDefinition"
                            args = ["CSSC", "CSSL", "FIMPort", "GSSG", "GSSL", "LSSC", "LSSG", "LSSL", "SCCS", "SCLS", "SCST", "SGGS", "SGLS", "SGST", "SLCS", "SLGS", "SLLS", "SLST", "STSC", "STSG", "STSL"]
                            
                    class EMBedding(SCPINodeN, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:BALanced:EMBedding
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "EMBedding"
                        args = ["1", "OFF", "ON"]
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters
                            
                            Arguments: 
                            """
                            _cmd = "PARameters"
                            args = [""]
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8ec140379660414a.htm#ID_abf3f1e2fa8e05b80a00206a01a47cb4-e08b0c9ffa8e002a0a00206a01a6673d-en-US>`_
                                
                                Arguments: CSSC, CSSL, GSSG, GSSL, LSSC, LSSG, SCCS, SCLS, SCST, SGGS, SGLS, SGST, SLCS, SLGS, STSC, STSG
                                """
                                _cmd = "C"
                                args = ["CSSC", "CSSL", "GSSG", "GSSL", "LSSC", "LSSG", "SCCS", "SCLS", "SCST", "SGGS", "SGLS", "SGST", "SLCS", "SLGS", "STSC", "STSG"]
                                
                            class DATA(SCPINodeN, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:DATA
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/079e83a8c9584f42.htm#ID_5d9cf2fb842de70c0a00201900076709-7b992475842de5850a00201901936165-en-US>`_
                                
                                Arguments: FPORts, IPORts
                                """
                                _cmd = "DATA"
                                args = ["FPORts", "IPORts"]
                                
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:G
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2ccae92408394fe5.htm#ID_7dea03e06f66334e0a001ae707928781-33d95ab56f6631c70a001ae727f5f310-en-US>`_
                                
                                Arguments: GSSG, GSSL, LSSG, SGGS, SGLS, SGST, SLGS, STSG
                                """
                                _cmd = "G"
                                args = ["GSSG", "GSSL", "LSSG", "SGGS", "SGLS", "SGST", "SLGS", "STSG"]
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a81a26b3e8d64942.htm#ID_ad04c1a1fa8e0d780a00206a0035eeba-bf4cbae4fa8e07ac0a00206a01a6673d-en-US>`_
                                
                                Arguments: CSSL, GSSL, LSSC, LSSG, LSSL, SCLS, SGLS, SLCS, SLGS, SLLS, SLST, STSL
                                """
                                _cmd = "L"
                                args = ["CSSL", "GSSL", "LSSC", "LSSG", "LSSL", "SCLS", "SGLS", "SLCS", "SLGS", "SLLS", "SLST", "STSL"]
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/45b9a3fe38f24521.htm#ID_f782d205fa8e15290a00206a00731edf-a1857f58fa8e0f6c0a00206a01a6673d-en-US>`_
                                
                                Arguments: CSSC, CSSL, GSSL, LSSC, LSSG, LSSL, SCCS, SCLS, SCST, SGLS, SLCS, SLGS, SLLS, SLST, STSC, STSL
                                """
                                _cmd = "R"
                                args = ["CSSC", "CSSL", "GSSL", "LSSC", "LSSG", "LSSL", "SCCS", "SCLS", "SCST", "SGLS", "SLCS", "SLGS", "SLLS", "SLST", "STSC", "STSL"]
                                
                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0941b76a5f064868.htm#ID_4cee94dffa8e242c0a00206a001fceaf-644e4ad9fa8e1e8f0a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:BALanced:EMBedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2c2c0962a3db4ae5.htm#ID_44ab70c2fa8e1cab0a00206a0136415c-a9f9c620fa8e16fd0a00206a01a6673d-en-US>`_
                            
                            Arguments: CSSC, CSSL, FIMPort, GSSG, GSSL, LSSC, LSSG, LSSL, SCCS, SCLS, SCST, SGGS, SGLS, SGST, SLCS, SLGS, SLLS, SLST, STSC, STSG, STSL
                            """
                            _cmd = "TNDefinition"
                            args = ["CSSC", "CSSL", "FIMPort", "GSSG", "GSSL", "LSSC", "LSSG", "LSSL", "SCCS", "SCLS", "SCST", "SGGS", "SGLS", "SGST", "SLCS", "SLGS", "SLLS", "SLST", "STSC", "STSG", "STSL"]
                            
                class DIFFerential(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:DIFFerential
                    
                    Arguments: 
                    """
                    _cmd = "DIFFerential"
                    args = [""]
                    
                    class EMBedding(SCPINodeN, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "EMBedding"
                        args = ["1", "OFF", "ON"]
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:PARameters
                            
                            Arguments: 
                            """
                            _cmd = "PARameters"
                            args = [""]
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/80c9a3cffb4f4e17.htm#ID_429e54d35811f7050a001ae7223f1761-c3650e9b5811f5500a001ae75f9ff217-en-US>`_
                                
                                Arguments: SHLC
                                """
                                _cmd = "C"
                                args = ["SHLC"]
                                
                            class DATA(SCPINodeN, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:PARameters:DATA
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ba87af15592944b1.htm#ID_6111424c5811f9d40a001ae752b7f8db-8e717b935811f84d0a001ae75f9ff217-en-US>`_
                                
                                Arguments: FPORts, IPORts
                                """
                                _cmd = "DATA"
                                args = ["FPORts", "IPORts"]
                                
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:PARameters:G
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4b188e3593414a28.htm#ID_0fc049035811fc830a001ae77896ac76-12d2ae9f5811fb0c0a001ae75f9ff217-en-US>`_
                                
                                Arguments: SHLC
                                """
                                _cmd = "G"
                                args = ["SHLC"]
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1e62e495ff464265.htm#ID_e5653d405811ff140a001ae77606ea04-ba2c9fd65811fd7d0a001ae75f9ff217-en-US>`_
                                
                                Arguments: SHLC
                                """
                                _cmd = "L"
                                args = ["SHLC"]
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f95acab1da68435d.htm#ID_ed781559581202110a001ae74e1270a2-65654e575812004c0a001ae75f9ff217-en-US>`_
                                
                                Arguments: SHLC
                                """
                                _cmd = "R"
                                args = ["SHLC"]
                                
                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/148b0faee7ee405f.htm#ID_54768ad0581204d00a001ae71ebb62bb-6c8d7c8c5812031b0a001ae75f9ff217-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:DIFFerential:EMBedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/fa133c6be7354958.htm#ID_63150e8d581207700a001ae7722d3053-8579f2a0581205ab0a001ae75f9ff217-en-US>`_
                            
                            Arguments: FIMPort, SHLC
                            """
                            _cmd = "TNDefinition"
                            args = ["FIMPort", "SHLC"]
                            
                class FSIMulator(SCPINode, SCPIBool):
                    """
                    CALCulate:TRANsform:VNETworks:FSIMulator
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "FSIMulator"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `CALCulate:TRANsform:VNETworks:FSIMulator:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d757c633360247c7.htm#ID_11fd85585d2ecf890a001ae7384a35ab-7de5b54a5d2ecdd30a001ae75392d2c4-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class GLOop(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:GLOop
                    
                    Arguments: 
                    """
                    _cmd = "GLOop"
                    args = [""]
                    
                    class DEEMbedding(SCPINode, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "DEEMbedding"
                        args = ["1", "OFF", "ON"]
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters
                            
                            Arguments: 
                            """
                            _cmd = "PARameters"
                            args = [""]
                            
                            class C(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/77956e5cf93946b3.htm#ID_81fff10dfa8e2bae0a00206a01a4b72d-5b3e5f86fa8e26110a00206a01a6673d-en-US>`_
                                
                                Arguments: SC, SG
                                """
                                _cmd = "C"
                                args = ["SC", "SG"]
                                
                            class G(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:G
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/aac6592ce85444e2.htm#ID_f8b2f8696f6642710a001ae710afca50-2f4c4e8c6f6640fa0a001ae727f5f310-en-US>`_
                                
                                Arguments: SG
                                """
                                _cmd = "G"
                                args = ["SG"]
                                
                            class L(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7a422b2f995d4f9a.htm#ID_a8965c72fa8e338e0a00206a0026bd75-609f9708fa8e2d830a00206a01a6673d-en-US>`_
                                
                                Arguments: SL
                                """
                                _cmd = "L"
                                args = ["SL"]
                                
                            class R(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5a1c1c036d584ff6.htm#ID_c0cffff5fa8e3b1f0a00206a008fe948-51c74c06fa8e35720a00206a01a6673d-en-US>`_
                                
                                Arguments: SC, SL
                                """
                                _cmd = "R"
                                args = ["SC", "SL"]
                                
                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/97f3857893904d79.htm#ID_159ddfd4fa8e4a330a00206a013b7c49-dc269bc4fa8e44a50a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:DEEMbedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/799259b2b62f4149.htm#ID_2f36ab34fa8e42c00a00206a01fc84f3-043babf2fa8e3d040a00206a01a6673d-en-US>`_
                            
                            Arguments: FIMPort, SC, SG, SL
                            """
                            _cmd = "TNDefinition"
                            args = ["FIMPort", "SC", "SG", "SL"]
                            
                    class EMBedding(SCPINode, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:GLOop:EMBedding
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "EMBedding"
                        args = ["1", "OFF", "ON"]
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters
                            
                            Arguments: 
                            """
                            _cmd = "PARameters"
                            args = [""]
                            
                            class C(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5ea6451ed3a94d89.htm#ID_37668013fa8e51d40a00206a00c15700-894bed2efa8e4c360a00206a01a6673d-en-US>`_
                                
                                Arguments: SC, SG
                                """
                                _cmd = "C"
                                args = ["SC", "SG"]
                                
                            class G(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:G
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/53607605721e41d0.htm#ID_dc37fee66f664fb00a001ae766fe6587-ed213d396f664dfa0a001ae727f5f310-en-US>`_
                                
                                Arguments: SG
                                """
                                _cmd = "G"
                                args = ["SG"]
                                
                            class L(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6c564130695147b8.htm#ID_b2cd795dfa8e59840a00206a01453521-97ac064cfa8e53b80a00206a01a6673d-en-US>`_
                                
                                Arguments: SL
                                """
                                _cmd = "L"
                                args = ["SL"]
                                
                            class R(SCPINode, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dbd85ab533b642e6.htm#ID_ed15dbb6fa8e61640a00206a01db511f-4a7a9660fa8e5b690a00206a01a6673d-en-US>`_
                                
                                Arguments: SC, SL
                                """
                                _cmd = "R"
                                args = ["SC", "SL"]
                                
                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f05d33e191e54ad2.htm#ID_337b7158fa8e70970a00206a01e3e1bf-ad84cdf0fa8e6ada0a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:GLOop:EMBedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/99b65e02d497406d.htm#ID_756d6eb0fa8e68e60a00206a008cf339-f9a8da34fa8e63390a00206a01a6673d-en-US>`_
                            
                            Arguments: FIMPort, SC, SG, SL
                            """
                            _cmd = "TNDefinition"
                            args = ["FIMPort", "SC", "SG", "SL"]
                            
                class PPAir(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:PPAir
                    
                    Arguments: 
                    """
                    _cmd = "PPAir"
                    args = [""]
                    
                    class DEEMbedding(SCPINodeN, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "DEEMbedding"
                        args = ["1", "OFF", "ON"]
                        
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:DEFine
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e8becb0a3078421b.htm#ID_3ba674b458120daa0a001ae715a0e5be-c703d9d69646cc8e0a001ae72394529b-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "DEFine"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class DELete(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:DELete
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/43d0e6d7b4144b08.htm#ID_1722509658120fbd0a001ae75e11b532-0381552758120e750a001ae75f9ff217-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "DELete"
                            args = [""]
                            
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters
                            
                            Arguments: 
                            """
                            _cmd = "PARameters"
                            args = [""]
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:C
                                
                                Arguments: CSSC, CSSL, GSSG, GSSL, LSSC, LSSG, SCCS, SCLS, SCST, SGGS, SGLS, SGST, SLCS, SLGS, STSC, STSG
                                """
                                _cmd = "C"
                                args = ["CSSC", "CSSL", "GSSG", "GSSL", "LSSC", "LSSG", "SCCS", "SCLS", "SCST", "SGGS", "SGLS", "SGST", "SLCS", "SLGS", "STSC", "STSG"]
                                
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:G
                                
                                Arguments: GSSG, GSSL, LSSG, SGGS, SGLS, SGST, SLGS, STSG
                                """
                                _cmd = "G"
                                args = ["GSSG", "GSSL", "LSSG", "SGGS", "SGLS", "SGST", "SLGS", "STSG"]
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:L
                                
                                Arguments: CSSL, GSSL, LSSC, LSSG, LSSL, SCLS, SGLS, SLCS, SLGS, SLLS, SLST, STSL
                                """
                                _cmd = "L"
                                args = ["CSSL", "GSSL", "LSSC", "LSSG", "LSSL", "SCLS", "SGLS", "SLCS", "SLGS", "SLLS", "SLST", "STSL"]
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:PARameters:R
                                
                                Arguments: CSSC, CSSL, GSSL, LSSC, LSSG, LSSL, SCCS, SCLS, SCST, SGLS, SLCS, SLGS, SLLS, SLST, STSC, STSL
                                """
                                _cmd = "R"
                                args = ["CSSC", "CSSL", "GSSL", "LSSC", "LSSG", "LSSL", "SCCS", "SCLS", "SCST", "SGLS", "SLCS", "SLGS", "SLLS", "SLST", "STSC", "STSL"]
                                
                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/46b480af07bb407f.htm#ID_4b3324f7581218d60a001ae751738823-c02afe855812176e0a001ae75f9ff217-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:DEEMbedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/35ec3220c32e4f80.htm#ID_3c16a3b758121b560a001ae77271577c-a49e9fde581219ef0a001ae75f9ff217-en-US>`_
                            
                            Arguments: CSSC, CSSL, FIMPort, GSSG, GSSL, LSSC, LSSG, LSSL, SCCS, SCLS, SCST, SGGS, SGLS, SGST, SLCS, SLGS, SLLS, SLST, STSC, STSG, STSL
                            """
                            _cmd = "TNDefinition"
                            args = ["CSSC", "CSSL", "FIMPort", "GSSG", "GSSL", "LSSC", "LSSG", "LSSL", "SCCS", "SCLS", "SCST", "SGGS", "SGLS", "SGST", "SLCS", "SLGS", "SLLS", "SLST", "STSC", "STSG", "STSL"]
                            
                    class EMBedding(SCPINodeN, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:PPAir:EMBedding
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "EMBedding"
                        args = ["1", "OFF", "ON"]
                        
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:DEFine
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e400839544a94301.htm#ID_e83fd23258121d790a001ae73123507a-8e751156970d6a920a001ae74f7a64ee-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "DEFine"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class DELete(SCPINode, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:DELete
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6c61769117054661.htm#ID_6ae62e5b58121ffa0a001ae712441e42-cabb03ec58121e540a001ae75f9ff217-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "DELete"
                            args = [""]
                            
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters
                            
                            Arguments: 
                            """
                            _cmd = "PARameters"
                            args = [""]
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:C
                                
                                Arguments: CSSC, CSSL, GSSG, GSSL, LSSC, LSSG, SCCS, SCLS, SCST, SGGS, SGLS, SGST, SLCS, SLGS, STSC, STSG
                                """
                                _cmd = "C"
                                args = ["CSSC", "CSSL", "GSSG", "GSSL", "LSSC", "LSSG", "SCCS", "SCLS", "SCST", "SGGS", "SGLS", "SGST", "SLCS", "SLGS", "STSC", "STSG"]
                                
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:G
                                
                                Arguments: GSSG, GSSL, LSSG, SGGS, SGLS, SGST, SLGS, STSG
                                """
                                _cmd = "G"
                                args = ["GSSG", "GSSL", "LSSG", "SGGS", "SGLS", "SGST", "SLGS", "STSG"]
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:L
                                
                                Arguments: CSSL, GSSL, LSSC, LSSG, LSSL, SCLS, SGLS, SLCS, SLGS, SLLS, SLST, STSL
                                """
                                _cmd = "L"
                                args = ["CSSL", "GSSL", "LSSC", "LSSG", "LSSL", "SCLS", "SGLS", "SLCS", "SLGS", "SLLS", "SLST", "STSL"]
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                CALCulate:TRANsform:VNETworks:PPAir:EMBedding:PARameters:R
                                
                                Arguments: CSSC, CSSL, GSSL, LSSC, LSSG, LSSL, SCCS, SCLS, SCST, SGLS, SLCS, SLGS, SLLS, SLST, STSC, STSL
                                """
                                _cmd = "R"
                                args = ["CSSC", "CSSL", "GSSL", "LSSC", "LSSG", "LSSL", "SCCS", "SCLS", "SCST", "SGLS", "SLCS", "SLGS", "SLLS", "SLST", "STSC", "STSL"]
                                
                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/db97017adcc64a9d.htm#ID_d3a37976581229510a001ae71520611c-bfc8ef34581227ca0a001ae75f9ff217-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PPAir:EMBedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f4fd86459812485c.htm#ID_85b0b37258122b930a001ae750c1f98b-d10f3fff58122a0c0a001ae75f9ff217-en-US>`_
                            
                            Arguments: CSSC, CSSL, FIMPort, GSSG, GSSL, LSSC, LSSG, LSSL, SCCS, SCLS, SCST, SGGS, SGLS, SGST, SLCS, SLGS, SLLS, SLST, STSC, STSG, STSL
                            """
                            _cmd = "TNDefinition"
                            args = ["CSSC", "CSSL", "FIMPort", "GSSG", "GSSL", "LSSC", "LSSG", "LSSL", "SCCS", "SCLS", "SCST", "SGGS", "SGLS", "SGST", "SLCS", "SLGS", "SLLS", "SLST", "STSC", "STSG", "STSL"]
                            
                class PSET(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:PSET
                    
                    Arguments: 
                    """
                    _cmd = "PSET"
                    args = [""]
                    
                    class DEEMbedding(SCPINodeN):
                        """
                        CALCulate:TRANsform:VNETworks:PSET:DEEMbedding
                        
                        Arguments: 
                        """
                        _cmd = "DEEMbedding"
                        args = [""]
                        
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PSET:DEEMbedding:DEFine
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/481a0c5b67654aaf.htm#ID_a38b0ffd97e86de70a001ae7390e6333-de29757a97e86c8f0a001ae760f7f904-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "DEFine"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                    class EMBedding(SCPINodeN):
                        """
                        CALCulate:TRANsform:VNETworks:PSET:EMBedding
                        
                        Arguments: 
                        """
                        _cmd = "EMBedding"
                        args = [""]
                        
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:PSET:EMBedding:DEFine
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f6b188400f7d4c8e.htm#ID_2cfc1d2497e86fbb0a001ae70cbfb36f-5d787a8997e86e830a001ae760f7f904-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "DEFine"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                class SENDed(SCPINode):
                    """
                    CALCulate:TRANsform:VNETworks:SENDed
                    
                    Arguments: 
                    """
                    _cmd = "SENDed"
                    args = [""]
                    
                    class DEEMbedding(SCPINodeN, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "DEEMbedding"
                        args = ["1", "OFF", "ON"]
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters
                            
                            Arguments: 
                            """
                            _cmd = "PARameters"
                            args = [""]
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8f37b1c2acee44bf.htm#ID_5ef9469cfa8e78470a00206a003fb9da-e1c64a86fa8e727b0a00206a01a6673d-en-US>`_
                                
                                Arguments: CSC, CSL, GSG, GSL, LSC, LSG, SCC, SCL, SGG, SGL, SHLC, SLC, SLG
                                """
                                _cmd = "C"
                                args = ["CSC", "CSL", "GSG", "GSL", "LSC", "LSG", "SCC", "SCL", "SGG", "SGL", "SHLC", "SLC", "SLG"]
                                
                            class DATA(SCPINodeN, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:DATA
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9fd3cb7e82ed444d.htm#ID_367ed7c5842dee7e0a0020190086f675-49915501842decb90a00201901936165-en-US>`_
                                
                                Arguments: FPORts, IPORts
                                """
                                _cmd = "DATA"
                                args = ["FPORts", "IPORts"]
                                
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:G
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c51043739b194e65.htm#ID_7cd42ef3aac442490a00201901b51a4b-b2bda20baac440650a002019014405dd-en-US>`_
                                
                                Arguments: GSG, GSL, LSG, SGG, SGL, SHLC, SLG
                                """
                                _cmd = "G"
                                args = ["GSG", "GSL", "LSG", "SGG", "SGL", "SHLC", "SLG"]
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ee2ffa524efe4143.htm#ID_ae17b162fa8e7fe80a00206a01b10570-63778782fa8e7a3b0a00206a01a6673d-en-US>`_
                                
                                Arguments: CSL, GSL, LSC, LSG, LSL, SCL, SGL, SHLC, SLC, SLG, SLL
                                """
                                _cmd = "L"
                                args = ["CSL", "GSL", "LSC", "LSG", "LSL", "SCL", "SGL", "SHLC", "SLC", "SLG", "SLL"]
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/fd7eabf9c9fe4f75.htm#ID_65259074fa8e877a0a00206a01c1d949-59bdb169fa8e81cd0a00206a01a6673d-en-US>`_
                                
                                Arguments: CSC, CSL, GSL, LSC, LSG, LSL, SCC, SCL, SGL, SHLC, SLC, SLG, SLL
                                """
                                _cmd = "R"
                                args = ["CSC", "CSL", "GSL", "LSC", "LSG", "LSL", "SCC", "SCL", "SGL", "SHLC", "SLC", "SLG", "SLL"]
                                
                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/099a019b9af84e28.htm#ID_4425e038fa8e96ad0a00206a00a9bdd8-133ea7b3fa8e90ff0a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:DEEMbedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/adbe16aed5bc4ba6.htm#ID_193f4b02fa8e8f2b0a00206a01d1a2a2-594a30cefa8e895e0a00206a01a6673d-en-US>`_
                            
                            Arguments: CSC, CSL, FIMPort, GSG, GSL, LSC, LSG, LSL, SCC, SCL, SGG, SGL, SHLC, SLC, SLG, SLL
                            """
                            _cmd = "TNDefinition"
                            args = ["CSC", "CSL", "FIMPort", "GSG", "GSL", "LSC", "LSG", "LSL", "SCC", "SCL", "SGG", "SGL", "SHLC", "SLC", "SLG", "SLL"]
                            
                    class EMBedding(SCPINodeN, SCPIBool):
                        """
                        CALCulate:TRANsform:VNETworks:SENDed:EMBedding
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "EMBedding"
                        args = ["1", "OFF", "ON"]
                        
                        class PARameters(SCPINode):
                            """
                            CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters
                            
                            Arguments: 
                            """
                            _cmd = "PARameters"
                            args = [""]
                            
                            class C(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:C
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9b3802e99dd04934.htm#ID_47ea57dcfa8e9e5d0a00206a01f8e797-a5454548fa8e98a00a00206a01a6673d-en-US>`_
                                
                                Arguments: CSC, CSL, GSG, GSL, LSC, LSG, SCC, SCL, SGG, SGL, SHLC, SLC, SLG
                                """
                                _cmd = "C"
                                args = ["CSC", "CSL", "GSG", "GSL", "LSC", "LSG", "SCC", "SCL", "SGG", "SGL", "SHLC", "SLC", "SLG"]
                                
                            class DATA(SCPINodeN, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:DATA
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bc40013c1fd34de5.htm#ID_792b4296842df3210a00201901d6e9a7-4e187817842df19b0a00201901936165-en-US>`_
                                
                                Arguments: FPORts, IPORts
                                """
                                _cmd = "DATA"
                                args = ["FPORts", "IPORts"]
                                
                            class G(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:G
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c2e016fdee4e41e6.htm#ID_bcec6412aac4474a0a00201900615633-9bb80280aac445370a002019014405dd-en-US>`_
                                
                                Arguments: GSG, GSL, LSG, SGG, SGL, SHLC, SLG
                                """
                                _cmd = "G"
                                args = ["GSG", "GSL", "LSG", "SGG", "SGL", "SHLC", "SLG"]
                                
                            class L(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:L
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/39cdaea4416a4c45.htm#ID_3c73b93dfa9057760a00206a0177c3c0-94278c7cfa9051a90a00206a01a6673d-en-US>`_
                                
                                Arguments: CSL, GSL, LSC, LSG, LSL, SCL, SGL, SHLC, SLC, SLG, SLL
                                """
                                _cmd = "L"
                                args = ["CSL", "GSL", "LSC", "LSG", "LSL", "SCL", "SGL", "SHLC", "SLC", "SLG", "SLL"]
                                
                            class R(SCPINodeN, SCPIQuery, SCPISet):
                                """
                                `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:PARameters:R
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/60828f5f8b0946d5.htm#ID_06bb1196fa905f070a00206a01dc29e4-44a83d6cfa90595a0a00206a01a6673d-en-US>`_
                                
                                Arguments: CSC, CSL, GSL, LSC, LSG, LSL, SCC, SCL, SGL, SHLC, SLC, SLG, SLL
                                """
                                _cmd = "R"
                                args = ["CSC", "CSL", "GSL", "LSC", "LSG", "LSL", "SCC", "SCL", "SGL", "SHLC", "SLC", "SLG", "SLL"]
                                
                        class STATe(SCPINode, SCPIBool):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ea669d4abf8a4e28.htm#ID_b1752cc1fa906e1a0a00206a01a677d6-a6a35038fa90685e0a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                        class TNDefinition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CALCulate:TRANsform:VNETworks:SENDed:EMBedding:TNDefinition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9741b5a2d5bc4f7b.htm#ID_8abb2864fa9066890a00206a0099762f-e45993bafa9060dc0a00206a01a6673d-en-US>`_
                            
                            Arguments: CSC, CSL, FIMPort, GSG, GSL, LSC, LSG, LSL, SCC, SCL, SGG, SGL, SHLC, SLC, SLG, SLL
                            """
                            _cmd = "TNDefinition"
                            args = ["CSC", "CSL", "FIMPort", "GSG", "GSL", "LSC", "LSG", "LSL", "SCC", "SCL", "SGG", "SGL", "SHLC", "SLC", "SLG", "SLL"]
                            
    class CONFigure(SCPINode):
        """
        CONFigure
        
        Arguments: 
        """
        _cmd = "CONFigure"
        args = [""]
        
        class CHANnel(SCPINodeN, SCPIBool):
            """
            CONFigure:CHANnel
            
            Arguments: 1, OFF, ON
            """
            _cmd = "CHANnel"
            args = ["1", "OFF", "ON"]
            
            class CATalog(SCPINode, SCPIQuery):
                """
                `CONFigure:CHANnel:CATalog
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e84155.htm#ID_8267d8bffa90756d0a00206a012834d2-871f66dffa906fe00a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "CATalog"
                args = [""]
                
            class MEASure(SCPINode, SCPIBool):
                """
                CONFigure:CHANnel:MEASure
                
                Arguments: 1, OFF, ON
                """
                _cmd = "MEASure"
                args = ["1", "OFF", "ON"]
                
                class ALL(SCPINode, SCPIBool):
                    """
                    CONFigure:CHANnel:MEASure:ALL
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "ALL"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `CONFigure:CHANnel:MEASure:ALL:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e84187.htm#ID_958019b491dbf9e30a00206a01973116-3beacfd491dbf1670a00206a00e9ecac-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class STATe(SCPINode, SCPIBool):
                    """
                    `CONFigure:CHANnel:MEASure:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2cd5e872062a431e.htm#ID_1cd54e3791dc03680a00206a012bd79a-94a956b691dbfc250a00206a00e9ecac-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `CONFigure:CHANnel:NAME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a31923122bab4e11.htm#ID_c3f9c539fa907cef0a00206a008fc1b5-8cf66519fa9077420a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "NAME"
                args = ["'string'"]
                
                class ID(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONFigure:CHANnel:NAME:ID
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/da0a7bd5700f41f7.htm#ID_abefaec0fa9084b00a00206a000fc09f-f57f33a0fa907ec40a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "ID"
                    args = ["'string'"]
                    
            class STATe(SCPINode, SCPIBool):
                """
                `CONFigure:CHANnel:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5e82d96f75e24caa.htm#ID_2b6e28fdfa9093940a00206a00cd97da-23931b64fa908de70a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
            class TRACe(SCPINode):
                """
                CONFigure:CHANnel:TRACe
                
                Arguments: 
                """
                _cmd = "TRACe"
                args = [""]
                
                class CATalog(SCPINode, SCPIQuery):
                    """
                    `CONFigure:CHANnel:TRACe:CATalog
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/08f2ade572024bd1.htm#ID_516e93ea91dc10e50a00206a01e04d6b-a40a757391dc09640a00206a00e9ecac-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "CATalog"
                    args = [""]
                    
                class REName(SCPINode, SCPISet):
                    """
                    `CONFigure:CHANnel:TRACe:REName
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bbb28f18094c4ae3.htm#ID_21f2bb55fa908c030a00206a0107df1a-9e702520fa9086840a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "REName"
                    args = ["'string'"]
                    
        class TRACe(SCPINodeN):
            """
            CONFigure:TRACe
            
            Arguments: 
            """
            _cmd = "TRACe"
            args = [""]
            
            class CATalog(SCPINode, SCPIQuery):
                """
                `CONFigure:TRACe:CATalog
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e84513.htm#ID_bce7da14fa909b060a00206a01cbd9eb-e44e55bcfa9095780a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "CATalog"
                args = [""]
                
            class CHANnel(SCPINode):
                """
                CONFigure:TRACe:CHANnel
                
                Arguments: 
                """
                _cmd = "CHANnel"
                args = [""]
                
                class NAME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONFigure:TRACe:CHANnel:NAME
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f94c4fcfb8094e4b.htm#ID_860185e0fa90a2980a00206a0129ec0d-0cfb8c52fa909ceb0a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "NAME"
                    args = ["'string'"]
                    
                    class ID(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONFigure:TRACe:CHANnel:NAME:ID
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/67062066b08c4c45.htm#ID_a007ba5bfa90aa0a0a00206a01848bb0-2e75d305fa90a47c0a00206a01a6673d-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "ID"
                        args = ["'string'"]
                        
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `CONFigure:TRACe:NAME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7a040ceb2d3a4047.htm#ID_e80abd45fa90b18c0a00206a01f4249c-c4d0154ffa90abee0a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "NAME"
                args = ["'string'"]
                
                class ID(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONFigure:TRACe:NAME:ID
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1f10213a5d6b4a80.htm#ID_295113b4fa90b8fe0a00206a001dfba5-cb7079e8fa90b3700a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "ID"
                    args = ["'string'"]
                    
            class REName(SCPINode, SCPISet):
                """
                `CONFigure:TRACe:REName
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d4f06d994adb4ffa.htm#ID_18b7574dfa90c0af0a00206a01c49181-40592207fa90bad30a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "REName"
                args = ["'string'"]
                
            class WINDow(SCPINode, SCPIQuery, SCPISet):
                """
                `CONFigure:TRACe:WINDow
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/668ea0c870b04c50.htm#ID_5352b2a291dc2c4d0a00206a005b7de7-e194934291dc23a20a00206a00e9ecac-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "WINDow"
                args = ["'string'"]
                
                class TRACe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONFigure:TRACe:WINDow:TRACe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/46d9e1a8f3dd4c7f.htm#ID_148894f091dc38240a00206a01003829-5f3601f391dc2edd0a00206a00e9ecac-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "TRACe"
                    args = ["'string'"]
                    
    class CONTrol(SCPINodeN):
        """
        CONTrol
        
        Arguments: 
        """
        _cmd = "CONTrol"
        args = [""]
        
        class AUXiliary(SCPINode):
            """
            CONTrol:AUXiliary
            
            Arguments: 
            """
            _cmd = "AUXiliary"
            args = [""]
            
            class C(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:AUXiliary:C
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "C"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:AUXiliary:C:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e84931.htm#ID_a8a179f7fa90c8400a00206a0033f6f5-e626ca43fa90c2840a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
        class GPIO(SCPINodeN, SCPIBool):
            """
            CONTrol:GPIO
            
            Arguments: 1, OFF, ON
            """
            _cmd = "GPIO"
            args = ["1", "OFF", "ON"]
            
            class RANGe(SCPINode, SCPIQuery, SCPISet):
                """
                `CONTrol:GPIO:RANGe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/349c9f24f7b3433f.htm#ID_fbbe897d42ae65c80a001ae7294019ae-ea623ece42ae63b50a001ae769a5b4da-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "RANGe"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class SENSe(SCPINode):
                """
                CONTrol:GPIO:SENSe
                
                Arguments: 
                """
                _cmd = "SENSe"
                args = [""]
                
                class CURRent(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:GPIO:SENSe:CURRent
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/12d640f764314050.htm#ID_35b0fe9842ae69140a001ae7666f9572-5a4c017642ae66a30a001ae769a5b4da-en-US>`_
                    
                    Arguments: ALL
                    """
                    _cmd = "CURRent"
                    args = ["ALL"]
                    
                class SUMCurrent(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:GPIO:SENSe:SUMCurrent
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/341e4955993a40cd.htm#ID_1156e2c642ae6c6f0a001ae700b67a48-88f098063a4211160a001ae7584876d3-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "SUMCurrent"
                    args = ["1"]
                    
                class TRIGger(SCPINode, SCPISet):
                    """
                    `CONTrol:GPIO:SENSe:TRIGger
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5b1bfbc418d04401.htm#ID_eb45576a42ae6f1f0a001ae74d3d666e-3a5b4e6342ae6d2b0a001ae769a5b4da-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "TRIGger"
                    args = [""]
                    
                class VOLTage(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:GPIO:SENSe:VOLTage
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0c5bc6da7bd14099.htm#ID_c60899b442ae726a0a001ae74f5e9a67-4245ee9c42ae70480a001ae769a5b4da-en-US>`_
                    
                    Arguments: ALL
                    """
                    _cmd = "VOLTage"
                    args = ["ALL"]
                    
            class SHUNt(SCPINode, SCPIQuery):
                """
                `CONTrol:GPIO:SHUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6b7dba82d2514647.htm#ID_bd7421c342ae74cc0a001ae706243599-6a4affa442ae73450a001ae769a5b4da-en-US>`_
                
                Arguments: 
                """
                _cmd = "SHUNt"
                args = [""]
                
            class STATe(SCPINode, SCPIBool):
                """
                `CONTrol:GPIO:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/33808ac223674735.htm#ID_d3192ded066b0d0c0a001ae756c50460-6c688743066b0a5c0a001ae733608be0-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
            class TIME(SCPINode, SCPIQuery, SCPISet):
                """
                `CONTrol:GPIO:TIME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/555a3361fb7246a1.htm#ID_4da2a64342ae77e90a001ae7608b44b4-7c39984c42ae75f50a001ae769a5b4da-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "TIME"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class VOLTage(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:GPIO:VOLTage
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "VOLTage"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class DEFault(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:GPIO:VOLTage:DEFault
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6d98569ee4824333.htm#ID_8470b084066b0ffa0a001ae758e7691b-a4394381066b0dd70a001ae733608be0-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DEFault"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class OUTPut(SCPINode, SCPISet):
                    """
                    `CONTrol:GPIO:VOLTage:OUTPut
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/17e1726b8d244456.htm#ID_a95593b7066b13260a001ae702394225-a4f6f8d5066b10e40a001ae733608be0-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "OUTPut"
                    args = [""]
                    
        class HANDler(SCPINode):
            """
            CONTrol:HANDler
            
            Arguments: 
            """
            _cmd = "HANDler"
            args = [""]
            
            class A(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:A
                
                Arguments: 1
                """
                _cmd = "A"
                args = ["1"]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:A:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0f573cb5afe64caf.htm#ID_384549a9fa90d7630a00206a01da5d48-204d2afafa90d1970a00206a01a6673d-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:A:MODE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e9cbd6865a25403a.htm#ID_fd883255fa90cfc20a00206a01b43b71-8197967cfa90ca150a00206a01a6673d-en-US>`_
                    
                    Arguments: INPut, OUTPut
                    """
                    _cmd = "MODE"
                    args = ["INPut", "OUTPut"]
                    
            class B(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:B
                
                Arguments: 1
                """
                _cmd = "B"
                args = ["1"]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:B:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0f573cb5afe64caf.htm#ID_82e32087fa90e6480a00206a009d90d0-a680df72fa90e0aa0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:B:MODE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e9cbd6865a25403a.htm#ID_df1b2421fa90dec60a00206a001fe8f9-a8227d8efa90d9280a00206a01a6673d-en-US>`_
                    
                    Arguments: INPut, OUTPut
                    """
                    _cmd = "MODE"
                    args = ["INPut", "OUTPut"]
                    
            class C(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:C
                
                Arguments: 1
                """
                _cmd = "C"
                args = ["1"]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:C:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0f573cb5afe64caf.htm#ID_3f9af4e0fa90f57a0a00206a004e2c4f-374a812bfa90efec0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:C:MODE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e9cbd6865a25403a.htm#ID_30067fb2fa90ee180a00206a0024945a-45be43defa90e81c0a00206a01a6673d-en-US>`_
                    
                    Arguments: INPut, OUTPut
                    """
                    _cmd = "MODE"
                    args = ["INPut", "OUTPut"]
                    
            class D(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:D
                
                Arguments: 1
                """
                _cmd = "D"
                args = ["1"]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:D:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0f573cb5afe64caf.htm#ID_d89e93e0fa91044f0a00206a0185bd14-2a93a2aafa90fec10a00206a01a6673d-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:D:MODE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e9cbd6865a25403a.htm#ID_f1fbb137fa90fcec0a00206a011639d8-dc1e6f5bfa90f75f0a00206a01a6673d-en-US>`_
                    
                    Arguments: INPut, OUTPut
                    """
                    _cmd = "MODE"
                    args = ["INPut", "OUTPut"]
                    
            class E(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:E
                
                Arguments: 1
                """
                _cmd = "E"
                args = ["1"]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:E:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0f573cb5afe64caf.htm#ID_03af4eaaaaa71b910a00206a014d37c1-e591bdf3aaa710370a00206a00dee6b8-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]
                    
            class EXTension(SCPINode):
                """
                CONTrol:HANDler:EXTension
                
                Arguments: 
                """
                _cmd = "EXTension"
                args = [""]
                
                class INDex(SCPINode):
                    """
                    CONTrol:HANDler:EXTension:INDex
                    
                    Arguments: 
                    """
                    _cmd = "INDex"
                    args = [""]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `CONTrol:HANDler:EXTension:INDex:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e85415.htm#ID_9ab7d58afa9122e30a00206a00a25190-37519af1fa911d260a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class RTRigger(SCPINode):
                    """
                    CONTrol:HANDler:EXTension:RTRigger
                    
                    Arguments: 
                    """
                    _cmd = "RTRigger"
                    args = [""]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `CONTrol:HANDler:EXTension:RTRigger:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e85466.htm#ID_822beadefa912aa30a00206a00c2e325-f42ab4a7fa9124e70a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
            class F(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:F
                
                Arguments: 1
                """
                _cmd = "F"
                args = ["1"]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:F:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0f573cb5afe64caf.htm#ID_65360c0daaa728920a00206a01178ad5-9c82b188aaa71e7f0a00206a00dee6b8-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]
                    
            class G(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:G
                
                Arguments: 1
                """
                _cmd = "G"
                args = ["1"]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:G:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0f573cb5afe64caf.htm#ID_2f4e59f6aaa737090a00206a01d8c5a5-d3dd0524aaa72ae30a00206a00dee6b8-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]
                    
            class H(SCPINode, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:H
                
                Arguments: 1
                """
                _cmd = "H"
                args = ["1"]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:H:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0f573cb5afe64caf.htm#ID_84a2a7bcaaa7460c0a00206a01237959-7700b423aaa73a350a00206a00dee6b8-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "DATA"
                    args = ["1"]
                    
            class INPut(SCPINode, SCPIQuery):
                """
                `CONTrol:HANDler:INPut
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/70a4807bdab549b6.htm#ID_817928e6aaa7560a0a00206a010ca1ce-6f60b089aaa749770a00206a00dee6b8-en-US>`_
                
                Arguments: 
                """
                _cmd = "INPut"
                args = [""]
                
            class LOGic(SCPINode, SCPIQuery, SCPISet):
                """
                `CONTrol:HANDler:LOGic
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e85543.htm#ID_f78b1faaaaa766d30a00206a00cb9c6b-84654118aaa758e80a00206a00dee6b8-en-US>`_
                
                Arguments: NEGative, POSitive
                """
                _cmd = "LOGic"
                args = ["NEGative", "POSitive"]
                
            class OUTPut(SCPINodeN, SCPIQuery, SCPISet):
                """
                CONTrol:HANDler:OUTPut
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "OUTPut"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:OUTPut:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ef6b44dd6cba4bbd.htm#ID_eec504bdfa9113d00a00206a004e84e5-63c0c051fa910df40a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class USER(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:OUTPut:USER
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d384e87b03b14621.htm#ID_b6012b5ffa910c0f0a00206a00a5d890-7969a7c7fa9106240a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "USER"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class PASSfail(SCPINode):
                """
                CONTrol:HANDler:PASSfail
                
                Arguments: 
                """
                _cmd = "PASSfail"
                args = [""]
                
                class LOGic(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:PASSfail:LOGic
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e85730.htm#ID_2595b82eaaa775590a00206a007fcf6d-a5b09155aaa769530a00206a00dee6b8-en-US>`_
                    
                    Arguments: NEGative, POSitive
                    """
                    _cmd = "LOGic"
                    args = ["NEGative", "POSitive"]
                    
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:PASSfail:MODE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e85780.htm#ID_f9bf98a0aaa783340a00206a00322e82-b914a914aaa777ea0a00206a00dee6b8-en-US>`_
                    
                    Arguments: FAIL, NOWait, PASS
                    """
                    _cmd = "MODE"
                    args = ["FAIL", "NOWait", "PASS"]
                    
                class POLicy(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:PASSfail:POLicy
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e85864.htm#ID_c5cf67d0aaa791ca0a00206a00b576ef-911cc27baaa785c40a00206a00dee6b8-en-US>`_
                    
                    Arguments: ALLMeas, ALLTests
                    """
                    _cmd = "POLicy"
                    args = ["ALLMeas", "ALLTests"]
                    
                class SCOPe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:HANDler:PASSfail:SCOPe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e85914.htm#ID_8f644a34aaa7a10c0a00206a01c34f32-a532dcccaaa794f70a00206a00dee6b8-en-US>`_
                    
                    Arguments: CHANnel, GLOBal
                    """
                    _cmd = "SCOPe"
                    args = ["CHANnel", "GLOBal"]
                    
                class STATus(SCPINode, SCPIQuery):
                    """
                    `CONTrol:HANDler:PASSfail:STATus
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e85974.htm#ID_669da323aaa7adfd0a00206a01e58d7b-4babcd6caaa7a3eb0a00206a00dee6b8-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "STATus"
                    args = [""]
                    
            class RESet(SCPINode, SCPISet):
                """
                `CONTrol:HANDler:RESet
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e86021.htm#ID_feafcc0afa911b520a00206a01d0958a-3c810aa7fa9115c40a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "RESet"
                args = [""]
                
            class SWEepend(SCPINode, SCPIQuery, SCPISet):
                """
                `CONTrol:HANDler:SWEepend
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e86040.htm#ID_4b826235aaa7c8f70a00206a001fcebb-4e04fab1aaa7bc740a00206a00dee6b8-en-US>`_
                
                Arguments: CHANnel, GLOBal, SWEep
                """
                _cmd = "SWEepend"
                args = ["CHANnel", "GLOBal", "SWEep"]
                
        class RFFE(SCPINodeN):
            """
            CONTrol:RFFE
            
            Arguments: 
            """
            _cmd = "RFFE"
            args = [""]
            
            class COMMand(SCPINode):
                """
                CONTrol:RFFE:COMMand
                
                Arguments: 
                """
                _cmd = "COMMand"
                args = [""]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:RFFE:COMMand:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/aede8dcd348f4fab.htm#ID_3502760a066b1f8a0a001ae70c239c0e-3f81058e066b1d770a001ae733608be0-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "DATA"
                    args = ["'string'"]
                    
                class SEND(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:RFFE:COMMand:SEND
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/79a9cbb958e04a7e.htm#ID_7aebff11066b22b70a001ae7728c5d1d-199a3e2481dfee9f0a001ae738278eca-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "SEND"
                    args = ["1"]
                    
            class SETTings(SCPINode, SCPIBool):
                """
                CONTrol:RFFE:SETTings
                
                Arguments: 1, OFF, ON
                """
                _cmd = "SETTings"
                args = ["1", "OFF", "ON"]
                
                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:RFFE:SETTings:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/86e7d9e9c64a4b80.htm#ID_e0afbdf3066b25c40a001ae7374f4675-88aae4cd066b23820a001ae733608be0-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "FREQuency"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `CONTrol:RFFE:SETTings:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ad56e7c2cd4c4c48.htm#ID_6e7676fa066b28440a001ae71c2aa9ef-7614426b066b26ae0a001ae733608be0-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
                class VOLTage(SCPINode):
                    """
                    CONTrol:RFFE:SETTings:VOLTage
                    
                    Arguments: 
                    """
                    _cmd = "VOLTage"
                    args = [""]
                    
                    class HIGH(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:RFFE:SETTings:VOLTage:HIGH
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/40122cc0e02b4df5.htm#ID_b7836816066b2b330a001ae7691148d3-90a164dd966b72ac0a001ae70f280944-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "HIGH"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class IO(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:RFFE:SETTings:VOLTage:IO
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/40122cc0e02b4df5.htm#ID_911e89b3066b2da40a001ae73936a740-8055592b066b2bee0a001ae733608be0-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "IO"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class LOW(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:RFFE:SETTings:VOLTage:LOW
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/40122cc0e02b4df5.htm#ID_d872d092066b30630a001ae75ad2e77f-1722156d066b2e8e0a001ae733608be0-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "LOW"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
            class TEST(SCPINode):
                """
                CONTrol:RFFE:TEST
                
                Arguments: 
                """
                _cmd = "TEST"
                args = [""]
                
                class CLOCk(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:RFFE:TEST:CLOCk
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b623d921df9b4f32.htm#ID_fe07d53142ae8b900a001ae758d3d25c-b8f0fc1242ae89ac0a001ae769a5b4da-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "CLOCk"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                    class CURRent(SCPINode, SCPIQuery):
                        """
                        `CONTrol:RFFE:TEST:CLOCk:CURRent
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cf63963efbf84711.htm#ID_3cd0732c42ae8e010a001ae75c5ad3c2-4429f3c442ae8c3c0a001ae769a5b4da-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "CURRent"
                        args = [""]
                        
                    class RANGe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:RFFE:TEST:CLOCk:RANGe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/061fcdd33a664d9b.htm#ID_b8e7b1e542ae90ef0a001ae748dcafdb-9b5f956a42ae8ebd0a001ae769a5b4da-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "RANGe"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class SHUNt(SCPINode, SCPIQuery):
                        """
                        `CONTrol:RFFE:TEST:CLOCk:SHUNt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a097b0172bac467a.htm#ID_0040e34542ae940c0a001ae723843b24-39e947dc42ae92090a001ae769a5b4da-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "SHUNt"
                        args = [""]
                        
                    class VOLTage(SCPINode, SCPIQuery):
                        """
                        `CONTrol:RFFE:TEST:CLOCk:VOLTage
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ad2db797ce1b4cea.htm#ID_6518d5f142ae963f0a001ae71acaf860-caee3aea42ae94c80a001ae769a5b4da-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "VOLTage"
                        args = [""]
                        
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:RFFE:TEST:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b623d921df9b4f32.htm#ID_35850b0d42ae98ee0a001ae76f74a14f-6018214142ae97290a001ae769a5b4da-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                    class CURRent(SCPINode, SCPIQuery):
                        """
                        `CONTrol:RFFE:TEST:DATA:CURRent
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cf63963efbf84711.htm#ID_537f944742ae9b210a001ae70088b5f7-939cdca842ae998a0a001ae769a5b4da-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "CURRent"
                        args = [""]
                        
                    class RANGe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:RFFE:TEST:DATA:RANGe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/061fcdd33a664d9b.htm#ID_a9da484d42ae9d630a001ae73d1b6a0f-c9bffd9442ae9bbd0a001ae769a5b4da-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "RANGe"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class SHUNt(SCPINode, SCPIQuery):
                        """
                        `CONTrol:RFFE:TEST:DATA:SHUNt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a097b0172bac467a.htm#ID_f2c0b0ea42ae9fe40a001ae73ebe1fb5-e2f7c72442ae9e3e0a001ae769a5b4da-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "SHUNt"
                        args = [""]
                        
                    class VOLTage(SCPINode, SCPIQuery):
                        """
                        `CONTrol:RFFE:TEST:DATA:VOLTage
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ad2db797ce1b4cea.htm#ID_d3c20f9542aea2550a001ae70a28fff2-afd4132142aea0800a001ae769a5b4da-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "VOLTage"
                        args = [""]
                        
                class OUTPut(SCPINode, SCPISet):
                    """
                    `CONTrol:RFFE:TEST:OUTPut
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/349450bbd5474192.htm#ID_289491a342aea4b60a001ae74d95b063-a4001e9e42aea3100a001ae769a5b4da-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "OUTPut"
                    args = [""]
                    
                class SENSe(SCPINode):
                    """
                    CONTrol:RFFE:TEST:SENSe
                    
                    Arguments: 
                    """
                    _cmd = "SENSe"
                    args = [""]
                    
                    class TRIGger(SCPINode, SCPISet):
                        """
                        `CONTrol:RFFE:TEST:SENSe:TRIGger
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/fc2f1b2520ad41db.htm#ID_c198b37442aea6aa0a001ae7130ede53-e70d1ff942aea5520a001ae769a5b4da-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "TRIGger"
                        args = [""]
                        
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:RFFE:TEST:TIME
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1ca1753cb9764fdd.htm#ID_af8ff50e42aea93a0a001ae704b63f39-0e0a68da42aea7940a001ae769a5b4da-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "TIME"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class VIO(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:RFFE:TEST:VIO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b623d921df9b4f32.htm#ID_da79227042aeab7c0a001ae757fdcd9e-e24566a43418ad380a001ae71794a01a-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "VIO"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                    class CURRent(SCPINode, SCPIQuery):
                        """
                        `CONTrol:RFFE:TEST:VIO:CURRent
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cf63963efbf84711.htm#ID_ff86537a42aeadbf0a001ae77b7fad68-ab7e749634e4dd0f0a001ae74d4c8092-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "CURRent"
                        args = [""]
                        
                    class RANGe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:RFFE:TEST:VIO:RANGe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/061fcdd33a664d9b.htm#ID_28d100dc42aeb0300a001ae712cc756f-d539c15c3480c6fc0a001ae728c0b35f-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "RANGe"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class SHUNt(SCPINode, SCPIQuery):
                        """
                        `CONTrol:RFFE:TEST:VIO:SHUNt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a097b0172bac467a.htm#ID_626f704a42aeb2b00a001ae7326db161-465a75bf3483d4180a001ae71f7de4eb-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "SHUNt"
                        args = [""]
                        
                    class VOLTage(SCPINode, SCPIQuery):
                        """
                        `CONTrol:RFFE:TEST:VIO:VOLTage
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ad2db797ce1b4cea.htm#ID_1fe1f36c42aeb5120a001ae76970a3e7-6204744b34e588750a001ae75431d893-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "VOLTage"
                        args = [""]
                        
        class SEGMent(SCPINodeN):
            """
            CONTrol:SEGMent
            
            Arguments: 
            """
            _cmd = "SEGMent"
            args = [""]
            
            class SEQuence(SCPINodeN):
                """
                CONTrol:SEGMent:SEQuence
                
                Arguments: 
                """
                _cmd = "SEQuence"
                args = [""]
                
                class CLEar(SCPINode):
                    """
                    CONTrol:SEGMent:SEQuence:CLEar
                    
                    Arguments: 
                    """
                    _cmd = "CLEar"
                    args = [""]
                    
                    class ALL(SCPINode, SCPISet):
                        """
                        `CONTrol:SEGMent:SEQuence:CLEar:ALL
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dce45392f23d4cd1.htm#ID_ba1740ff066b32e30a001ae7038cc690-e385c4e6066b312e0a001ae733608be0-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "ALL"
                        args = [""]
                        
                class COUNt(SCPINode, SCPIQuery):
                    """
                    `CONTrol:SEGMent:SEQuence:COUNt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/863ad1f221e34a86.htm#ID_d8be4e36066b35060a001ae76687ab53-7eee6fdf066b33be0a001ae733608be0-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "COUNt"
                    args = [""]
                    
                class DELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:SEGMent:SEQuence:DELay
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cad27b08f5cd4a59.htm#ID_ff5337c49a5a3eae0a001ae7055abd97-52198a0c066b36ac0a001ae733608be0-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DELay"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class GPIO(SCPINodeN):
                    """
                    CONTrol:SEGMent:SEQuence:GPIO
                    
                    Arguments: 
                    """
                    _cmd = "GPIO"
                    args = [""]
                    
                    class VOLTage(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:SEGMent:SEQuence:GPIO:VOLTage
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d59396a2d7e04724.htm#ID_b11ac4b4066b3b210a001ae7511309cd-19aa6061066b394c0a001ae733608be0-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "VOLTage"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class RFFE(SCPINodeN):
                    """
                    CONTrol:SEGMent:SEQuence:RFFE
                    
                    Arguments: 
                    """
                    _cmd = "RFFE"
                    args = [""]
                    
                    class COMMand(SCPINode):
                        """
                        CONTrol:SEGMent:SEQuence:RFFE:COMMand
                        
                        Arguments: 
                        """
                        _cmd = "COMMand"
                        args = [""]
                        
                        class DATA(SCPINode, SCPIQuery, SCPISet):
                            """
                            `CONTrol:SEGMent:SEQuence:RFFE:COMMand:DATA
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/391f2dd3ce594a86.htm#ID_06ace371066b3e5d0a001ae77224664e-1fcbae3c066b3c0b0a001ae733608be0-en-US>`_
                            
                            Arguments: 'string'
                            """
                            _cmd = "DATA"
                            args = ["'string'"]
                            
        class SEQuence(SCPINodeN):
            """
            CONTrol:SEQuence
            
            Arguments: 
            """
            _cmd = "SEQuence"
            args = [""]
            
            class CLEar(SCPINode):
                """
                CONTrol:SEQuence:CLEar
                
                Arguments: 
                """
                _cmd = "CLEar"
                args = [""]
                
                class ALL(SCPINode, SCPISet):
                    """
                    `CONTrol:SEQuence:CLEar:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ae61df9a65994430.htm#ID_333f4491066b40ce0a001ae721c73f52-88df1fd0066b3f090a001ae733608be0-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "ALL"
                    args = [""]
                    
            class COUNt(SCPINode, SCPIQuery):
                """
                `CONTrol:SEQuence:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/17252f9e8804497b.htm#ID_f18ea6b6066b42f10a001ae70911d2e1-27e2fa22066b416a0a001ae733608be0-en-US>`_
                
                Arguments: 
                """
                _cmd = "COUNt"
                args = [""]
                
            class DELay(SCPINode, SCPIQuery, SCPISet):
                """
                `CONTrol:SEQuence:DELay
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0bb940016a74464e.htm#ID_d484ffa7066b45230a001ae716a8581a-0dce9372066b43ac0a001ae733608be0-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "DELay"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class GPIO(SCPINodeN):
                """
                CONTrol:SEQuence:GPIO
                
                Arguments: 
                """
                _cmd = "GPIO"
                args = [""]
                
                class VOLTage(SCPINode, SCPIQuery, SCPISet):
                    """
                    `CONTrol:SEQuence:GPIO:VOLTage
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3fb7df3527744c2b.htm#ID_61c443f1066b47850a001ae76731bb7b-8bcc6627066b460e0a001ae733608be0-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "VOLTage"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class RFFE(SCPINodeN):
                """
                CONTrol:SEQuence:RFFE
                
                Arguments: 
                """
                _cmd = "RFFE"
                args = [""]
                
                class COMMand(SCPINode):
                    """
                    CONTrol:SEQuence:RFFE:COMMand
                    
                    Arguments: 
                    """
                    _cmd = "COMMand"
                    args = [""]
                    
                    class DATA(SCPINode, SCPIQuery, SCPISet):
                        """
                        `CONTrol:SEQuence:RFFE:COMMand:DATA
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b78d712928e44350.htm#ID_fca5b214066b4a240a001ae74dd3450e-e2ac204e066b48500a001ae733608be0-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "DATA"
                        args = ["'string'"]
                        
    class DIAGnostic(SCPINode):
        """
        DIAGnostic
        
        Arguments: 
        """
        _cmd = "DIAGnostic"
        args = [""]
        
        class ALC(SCPINode):
            """
            DIAGnostic:ALC
            
            Arguments: 
            """
            _cmd = "ALC"
            args = [""]
            
            class SETTings(SCPINode, SCPIBool):
                """
                DIAGnostic:ALC:SETTings
                
                Arguments: 1, OFF, ON
                """
                _cmd = "SETTings"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    DIAGnostic:ALC:SETTings:STATe
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
        class DEFault(SCPINode, SCPIQuery, SCPISet):
            """
            DIAGnostic:DEFault
            
            Arguments: 
            """
            _cmd = "DEFault"
            args = [""]
            
        class DEVice(SCPINode):
            """
            DIAGnostic:DEVice
            
            Arguments: 
            """
            _cmd = "DEVice"
            args = [""]
            
            class STATe(SCPINode, SCPISet):
                """
                `DIAGnostic:DEVice:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e88039.htm#ID_4ccbc72a134d7a160a00206a00fc7723-c47502c8134d740b0a00206a0182dc26-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "STATe"
                args = ["'string'"]
                
        class DUMP(SCPINode):
            """
            DIAGnostic:DUMP
            
            Arguments: 
            """
            _cmd = "DUMP"
            args = [""]
            
            class SIZE(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:DUMP:SIZE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ff494033e9a843aa.htm#ID_a7bac880066b4d220a001ae71bbc7e0d-90f2c5f2066b4b9b0a001ae733608be0-en-US>`_
                
                Arguments: FULL, LARGe, MINI, NONE, NORMal
                """
                _cmd = "SIZE"
                args = ["FULL", "LARGe", "MINI", "NONE", "NORMal"]
                
        class PRODuct(SCPINode):
            """
            DIAGnostic:PRODuct
            
            Arguments: 
            """
            _cmd = "PRODuct"
            args = [""]
            
            class CATalog(SCPINode, SCPIQuery):
                """
                DIAGnostic:PRODuct:CATalog
                
                Arguments: 
                """
                _cmd = "CATalog"
                args = [""]
                
            class DESCription(SCPINode, SCPIQuery):
                """
                DIAGnostic:PRODuct:DESCription
                
                Arguments: 
                """
                _cmd = "DESCription"
                args = [""]
                
            class ID(SCPINode, SCPIQuery):
                """
                DIAGnostic:PRODuct:ID
                
                Arguments: 
                """
                _cmd = "ID"
                args = [""]
                
            class MACaddress(SCPINode, SCPIQuery):
                """
                DIAGnostic:PRODuct:MACaddress
                
                Arguments: 
                """
                _cmd = "MACaddress"
                args = [""]
                
            class OPTion(SCPINode):
                """
                DIAGnostic:PRODuct:OPTion
                
                Arguments: 
                """
                _cmd = "OPTion"
                args = [""]
                
                class FACTory(SCPINode):
                    """
                    DIAGnostic:PRODuct:OPTion:FACTory
                    
                    Arguments: 
                    """
                    _cmd = "FACTory"
                    args = [""]
                    
                    class CLEar(SCPINode, SCPISet):
                        """
                        DIAGnostic:PRODuct:OPTion:FACTory:CLEar
                        
                        Arguments: 
                        """
                        _cmd = "CLEar"
                        args = [""]
                        
                class INFO(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DIAGnostic:PRODuct:OPTion:INFO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0bab836e2f604f5e.htm#ID_5b4bc3d2a1e970ab0a001ae735fbde1d-a3143537a1e96f730a001ae70a9caa95-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "INFO"
                    args = ["'string'"]
                    
                class LICence(SCPINode):
                    """
                    DIAGnostic:PRODuct:OPTion:LICence
                    
                    Arguments: 
                    """
                    _cmd = "LICence"
                    args = [""]
                    
                    class CHECk(SCPINode, SCPIQuery, SCPISet):
                        """
                        DIAGnostic:PRODuct:OPTion:LICence:CHECk
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "CHECk"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class UNLock(SCPINode, SCPISet):
                        """
                        DIAGnostic:PRODuct:OPTion:LICence:UNLock
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "UNLock"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class LIST(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:PRODuct:OPTion:LIST
                    
                    Arguments: 
                    """
                    _cmd = "LIST"
                    args = [""]
                    
                class STATus(SCPINode, SCPIQuery, SCPISet):
                    """
                    DIAGnostic:PRODuct:OPTion:STATus
                    
                    Arguments: #<block, 'string'
                    """
                    _cmd = "STATus"
                    args = ["#<block", "'string'"]
                    
            class SELect(SCPINode, SCPIQuery, SCPISet):
                """
                DIAGnostic:PRODuct:SELect
                
                Arguments: 'string'
                """
                _cmd = "SELect"
                args = ["'string'"]
                
            class TIME(SCPINode):
                """
                DIAGnostic:PRODuct:TIME
                
                Arguments: 
                """
                _cmd = "TIME"
                args = [""]
                
                class OPERating(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:PRODuct:TIME:OPERating
                    
                    Arguments: 
                    """
                    _cmd = "OPERating"
                    args = [""]
                    
        class SERVice(SCPINode):
            """
            DIAGnostic:SERVice
            
            Arguments: 
            """
            _cmd = "SERVice"
            args = [""]
            
            class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:SERVice:FUNCtion
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e124271.htm#ID_351c4edbfa91942b0a00206a019938ad-c622f7b0fa918e7e0a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "FUNCtion"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class RFPower(SCPINode, SCPIBool):
                """
                `DIAGnostic:SERVice:RFPower
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e88126.htm#ID_05ffa5f6fa919bcc0a00206a006174c7-16a66f8cfa91960f0a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "RFPower"
                args = ["1", "OFF", "ON"]
                
            class SFUNction(SCPINode, SCPIQuery, SCPISet):
                """
                `DIAGnostic:SERVice:SFUNction
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f85cfd9d4d74448e.htm#ID_48fd1718fa91a33e0a00206a0034447a-4ce344b0fa919da10a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "SFUNction"
                args = ["'string'"]
                
        class UPDate(SCPINode):
            """
            DIAGnostic:UPDate
            
            Arguments: 
            """
            _cmd = "UPDate"
            args = [""]
            
            class BOOT(SCPINode, SCPISet):
                """
                DIAGnostic:UPDate:BOOT
                
                Arguments: 
                """
                _cmd = "BOOT"
                args = [""]
                
            class CATalog(SCPINode, SCPIQuery):
                """
                DIAGnostic:UPDate:CATalog
                
                Arguments: 
                """
                _cmd = "CATalog"
                args = [""]
                
            class CHAP(SCPINode):
                """
                DIAGnostic:UPDate:CHAP
                
                Arguments: 
                """
                _cmd = "CHAP"
                args = [""]
                
                class CHALlenge(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:UPDate:CHAP:CHALlenge
                    
                    Arguments: 
                    """
                    _cmd = "CHALlenge"
                    args = [""]
                    
                class PRESet(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:CHAP:PRESet
                    
                    Arguments: 
                    """
                    _cmd = "PRESet"
                    args = [""]
                    
                class RESPonse(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:CHAP:RESPonse
                    
                    Arguments: #<block
                    """
                    _cmd = "RESPonse"
                    args = ["#<block"]
                    
            class EXECute(SCPINode, SCPISet):
                """
                DIAGnostic:UPDate:EXECute
                
                Arguments: NOWait, OVERlay, WAIT
                """
                _cmd = "EXECute"
                args = ["NOWait", "OVERlay", "WAIT"]
                
            class INSTall(SCPINode, SCPISet):
                """
                DIAGnostic:UPDate:INSTall
                
                Arguments: 'string'
                """
                _cmd = "INSTall"
                args = ["'string'"]
                
                class BEGin(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:INSTall:BEGin
                    
                    Arguments: 
                    """
                    _cmd = "BEGin"
                    args = [""]
                    
                class END(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:INSTall:END
                    
                    Arguments: 
                    """
                    _cmd = "END"
                    args = [""]
                    
                class STATus(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:UPDate:INSTall:STATus
                    
                    Arguments: 
                    """
                    _cmd = "STATus"
                    args = [""]
                    
            class PROGress(SCPINode, SCPIQuery, SCPISet):
                """
                DIAGnostic:UPDate:PROGress
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "PROGress"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class TRANsfer(SCPINode):
                """
                DIAGnostic:UPDate:TRANsfer
                
                Arguments: 
                """
                _cmd = "TRANsfer"
                args = [""]
                
                class CLOSe(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:TRANsfer:CLOSe
                    
                    Arguments: 
                    """
                    _cmd = "CLOSe"
                    args = [""]
                    
                class DATA(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:TRANsfer:DATA
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class OPEN(SCPINode, SCPISet):
                    """
                    DIAGnostic:UPDate:TRANsfer:OPEN
                    
                    Arguments: DATA, DESCr
                    """
                    _cmd = "OPEN"
                    args = ["DATA", "DESCr"]
                    
                class VERSion(SCPINode, SCPIQuery):
                    """
                    DIAGnostic:UPDate:TRANsfer:VERSion
                    
                    Arguments: 
                    """
                    _cmd = "VERSion"
                    args = [""]
                    
    class DISPlay(SCPINode, SCPIBool):
        """
        DISPlay
        
        Arguments: 1, OFF, ON
        """
        _cmd = "DISPlay"
        args = ["1", "OFF", "ON"]
        
        class ANNotation(SCPINode):
            """
            DISPlay:ANNotation
            
            Arguments: 
            """
            _cmd = "ANNotation"
            args = [""]
            
            class CHANnel(SCPINode, SCPIBool):
                """
                DISPlay:ANNotation:CHANnel
                
                Arguments: 1, OFF, ON
                """
                _cmd = "CHANnel"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `DISPlay:ANNotation:CHANnel:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/97b83eb36eea4b22.htm#ID_09283553fa921c940a00206a00bfb2e1-8c3c7511fa9216e70a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class FREQuency(SCPINode, SCPIBool):
                """
                DISPlay:ANNotation:FREQuency
                
                Arguments: 1, OFF, ON
                """
                _cmd = "FREQuency"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `DISPlay:ANNotation:FREQuency:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a9752bf5700b4921.htm#ID_a0b6805dfa9224350a00206a01dcf415-e0bc5d8cfa921e880a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class TRACe(SCPINode, SCPIBool):
                """
                DISPlay:ANNotation:TRACe
                
                Arguments: 1, OFF, ON
                """
                _cmd = "TRACe"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `DISPlay:ANNotation:TRACe:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/97b83eb36eea4b22.htm#ID_69d46e9ebba79eea0a002019006f313f-268f85a2bba79dc10a0020190170f726-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
        class CMAP(SCPINodeN):
            """
            DISPlay:CMAP
            
            Arguments: 
            """
            _cmd = "CMAP"
            args = [""]
            
            class LIMit(SCPINode, SCPIBool):
                """
                DISPlay:CMAP:LIMit
                
                Arguments: 1, OFF, ON
                """
                _cmd = "LIMit"
                args = ["1", "OFF", "ON"]
                
                class FCOLorize(SCPINode, SCPIBool):
                    """
                    DISPlay:CMAP:LIMit:FCOLorize
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "FCOLorize"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `DISPlay:CMAP:LIMit:FCOLorize:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e88412.htm#ID_07203f1f996b99230a00206a01fea816-cd8545fd996b91050a00206a0049ced2-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class FSYMbol(SCPINode, SCPIBool):
                    """
                    DISPlay:CMAP:LIMit:FSYMbol
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "FSYMbol"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `DISPlay:CMAP:LIMit:FSYMbol:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e88444.htm#ID_a789ec67996ba7b90a00206a01775331-994b212d996b9e720a00206a0049ced2-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class STATe(SCPINode, SCPIBool):
                    """
                    `DISPlay:CMAP:LIMit:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e88473.htm#ID_b72519cea06b7a720a00206a006d9d2b-2c0171cca06b736d0a00206a013722ca-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class MARKer(SCPINode, SCPIBool):
                """
                DISPlay:CMAP:MARKer
                
                Arguments: 1, OFF, ON
                """
                _cmd = "MARKer"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `DISPlay:CMAP:MARKer:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e88523.htm#ID_e76ed6a7fa922c050a00206a00aef132-0ec64a50fa92261a0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class RGB(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:CMAP:RGB
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/752a679d99444b26.htm#ID_f96e2125fa9233b60a00206a0101687a-9f550bd8fa922dea0a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "RGB"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class TRACe(SCPINode):
                """
                DISPlay:CMAP:TRACe
                
                Arguments: 
                """
                _cmd = "TRACe"
                args = [""]
                
                class COLor(SCPINode, SCPIBool):
                    """
                    DISPlay:CMAP:TRACe:COLor
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "COLor"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `DISPlay:CMAP:TRACe:COLor:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e88839.htm#ID_96913623fa923b670a00206a01ee5bbf-923eb8ebfa9235aa0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class RGB(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:CMAP:TRACe:RGB
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e88887.htm#ID_71191c2cfa9243080a00206a015c1979-8ce5c12bfa923d4b0a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "RGB"
                    args = ["'string'"]
                    
        class LAYout(SCPINode, SCPIQuery, SCPISet):
            """
            `DISPlay:LAYout
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/620d9d36a28c4ad0.htm#ID_42356ef6aaa7d54b0a00206a001cddae-8913c9f4aaa7cafb0a00206a00dee6b8-en-US>`_
            
            Arguments: GRID, HORizontal, LINeup, STACk, VERTical
            """
            _cmd = "LAYout"
            args = ["GRID", "HORizontal", "LINeup", "STACk", "VERTical"]
            
            class APPLy(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:LAYout:APPLy
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5ec7955dbc1f4eea.htm#ID_d6f4fe84ced4d31c0a00201901c85cc7-1dabc1deced4d1c40a0020190170f726-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "APPLy"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class DEFine(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:LAYout:DEFine
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f39aa8b61fee48fd.htm#ID_4332cc0dbba7a40b0a0020190055a26c-111967f3bba7a2e20a0020190170f726-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "DEFine"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class EXECute(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:LAYout:EXECute
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ccb35e5e7c3b49fd.htm#ID_bd48f718bba7a5b10a002019009a678c-db3d473fbba7a4780a0020190170f726-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "EXECute"
                args = ["'string'"]
                
            class GRID(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:LAYout:GRID
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f0abcfab12584f77.htm#ID_70abfb19aaa7e2990a00206a01d81c00-a7770b8aaaa7d7cc0a00206a00dee6b8-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "GRID"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class JOIN(SCPINode, SCPISet):
                """
                `DISPlay:LAYout:JOIN
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/53c5effa46dc4646.htm#ID_000c4953bba7a7760a00201901e721c0-4109ca06bba7a65c0a0020190170f726-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "JOIN"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
        class MENU(SCPINode):
            """
            DISPlay:MENU
            
            Arguments: 
            """
            _cmd = "MENU"
            args = [""]
            
            class KEY(SCPINode):
                """
                DISPlay:MENU:KEY
                
                Arguments: 
                """
                _cmd = "KEY"
                args = [""]
                
                class ACTion(SCPINode):
                    """
                    DISPlay:MENU:KEY:ACTion
                    
                    Arguments: 
                    """
                    _cmd = "ACTion"
                    args = [""]
                    
                    class CATalog(SCPINode, SCPIQuery):
                        """
                        `DISPlay:MENU:KEY:ACTion:CATalog
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f6835e6d92de448c.htm#ID_40cd2d0f42aed01c0a001ae719dc4c53-7db06bd742aece950a001ae769a5b4da-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "CATalog"
                        args = [""]
                        
                class EXECute(SCPINode, SCPISet):
                    """
                    `DISPlay:MENU:KEY:EXECute
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5f9d9a82fa7a43c5.htm#ID_3cfeb142fa924ac80a00206a01a8df15-3262509dfa9244ec0a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "EXECute"
                    args = ["'string'"]
                    
                class SELect(SCPINode, SCPISet):
                    """
                    `DISPlay:MENU:KEY:SELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f6979f1d623948b8.htm#ID_2fd74a4efa92522b0a00206a00390f14-27eea583fa924c9d0a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "SELect"
                    args = ["'string'"]
                    
                class TOOL(SCPINode):
                    """
                    DISPlay:MENU:KEY:TOOL
                    
                    Arguments: 
                    """
                    _cmd = "TOOL"
                    args = [""]
                    
                    class CATalog(SCPINode, SCPIQuery):
                        """
                        `DISPlay:MENU:KEY:TOOL:CATalog
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a88b3c3cf6194874.htm#ID_52791e5d42aed3580a001ae725bfcd9e-fa48469242aed1830a001ae769a5b4da-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "CATalog"
                        args = [""]
                        
        class RFSize(SCPINode, SCPIQuery, SCPISet):
            """
            `DISPlay:RFSize
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e89588.htm#ID_26a7f2c7fa9259db0a00206a00f26a73-0ebe17bdfa9253ff0a00206a01a6673d-en-US>`_
            
            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "RFSize"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
            
        class WINDow(SCPINodeN, SCPIBool):
            """
            DISPlay:WINDow
            
            Arguments: 1, OFF, ON
            """
            _cmd = "WINDow"
            args = ["1", "OFF", "ON"]
            
            class CATalog(SCPINode, SCPIQuery):
                """
                `DISPlay:WINDow:CATalog
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/abdd1db5dc0c48ee.htm#ID_84400b55fa92616d0a00206a006ce5e8-2bbb3a15fa925bb00a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "CATalog"
                args = [""]
                
            class MAXimize(SCPINode, SCPIBool):
                """
                `DISPlay:WINDow:MAXimize
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/99dca8ff187d4000.htm#ID_f3f24319fa9268ef0a00206a01e4b6e2-f727d921fa9263420a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "MAXimize"
                args = ["1", "OFF", "ON"]
                
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `DISPlay:WINDow:NAME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2bf57f884ae84ed2.htm#ID_b9f0fbecfa9270de0a00206a00a45db7-1a416912fa926ad30a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "NAME"
                args = ["'string'"]
                
            class OVERview(SCPINode, SCPIBool):
                """
                DISPlay:WINDow:OVERview
                
                Arguments: 1, OFF, ON
                """
                _cmd = "OVERview"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `DISPlay:WINDow:OVERview:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/33fe4a73a2ab4070.htm#ID_10fbd8f3ced4d87b0a00201901b68cc7-1d9f9891ced4d7230a0020190170f726-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class STATe(SCPINode, SCPIBool):
                """
                `DISPlay:WINDow:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/065c895d5a2c4230.htm#ID_8e3cb1f5fa9278600a00206a01851f55-928f75e4fa9272b30a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
            class TITLe(SCPINode, SCPIBool):
                """
                DISPlay:WINDow:TITLe
                
                Arguments: 1, OFF, ON
                """
                _cmd = "TITLe"
                args = ["1", "OFF", "ON"]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:WINDow:TITLe:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ac203fe8a5b647c2.htm#ID_0f9ac45ffa9280010a00206a00e0d734-11ac0202fa927a540a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "DATA"
                    args = ["'string'"]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `DISPlay:WINDow:TITLe:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/30e7340225704fd9.htm#ID_c1d70c02fa9287a20a00206a009fab43-d77d2d0bfa9281f50a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class TRACe(SCPINodeN):
                """
                DISPlay:WINDow:TRACe
                
                Arguments: 
                """
                _cmd = "TRACe"
                args = [""]
                
                class CATalog(SCPINode, SCPIQuery):
                    """
                    `DISPlay:WINDow:TRACe:CATalog
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f6c8345f1d4348ad.htm#ID_906f0858fa928f340a00206a012e7faf-69a2c93cfa9289860a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "CATalog"
                    args = [""]
                    
                class DELete(SCPINode, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:DELete
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/35e75331f5ce4fce.htm#ID_9bdc6b44fa9296c50a00206a00b068cd-6a447b3ffa9291280a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "DELete"
                    args = [""]
                    
                class EFEed(SCPINode, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:EFEed
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a702a260a63d4a10.htm#ID_e3fa49acfa929e470a00206a01a34211-1ed47549fa9298a90a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "EFEed"
                    args = ["'string'"]
                    
                class FEED(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:FEED
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/58dad852e7db48a0.htm#ID_d87ac43bfa92a5f80a00206a01214a13-c23d3890fa92a02b0a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "FEED"
                    args = ["'string'"]
                    
                class SHOW(SCPINode, SCPIQuery, SCPISet):
                    """
                    `DISPlay:WINDow:TRACe:SHOW
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/666cb4f2f8874259.htm#ID_e087b135fa92ad990a00206a0109416c-3de7dacafa92a7ec0a00206a01a6673d-en-US>`_
                    
                    Arguments: DALL, MALL, 'string'
                    """
                    _cmd = "SHOW"
                    args = ["DALL", "MALL", "'string'"]
                    
                class X(SCPINode):
                    """
                    DISPlay:WINDow:TRACe:X
                    
                    Arguments: 
                    """
                    _cmd = "X"
                    args = [""]
                    
                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:X:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1efcc8fa102b4b9b.htm#ID_eb26dfc0fa92b51b0a00206a00214931-20aba55afa92af6d0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "OFFSet"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class Y(SCPINode):
                    """
                    DISPlay:WINDow:TRACe:Y
                    
                    Arguments: 
                    """
                    _cmd = "Y"
                    args = [""]
                    
                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:Y:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/fba6bb59b840434f.htm#ID_65233ce8fa92bcbc0a00206a0082ad31-db88fa1afa92b6ff0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "OFFSet"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class SCALe(SCPINode):
                        """
                        DISPlay:WINDow:TRACe:Y:SCALe
                        
                        Arguments: 
                        """
                        _cmd = "SCALe"
                        args = [""]
                        
                        class AUTO(SCPINode, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:AUTO
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b1fbc2b484774b76.htm#ID_1feb2da3fa92c42e0a00206a01e047da-37730b41fa92bea00a00206a01a6673d-en-US>`_
                            
                            Arguments: ONCE
                            """
                            _cmd = "AUTO"
                            args = ["ONCE"]
                            
                        class BOTTom(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:BOTTom
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6331132d7bf24ded.htm#ID_8b51ec30fa92cbdf0a00206a0123a5f0-4e44393dfa92c6120a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "BOTTom"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class PDIVision(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:PDIVision
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bdc5467b9ebd4d43.htm#ID_4c11fb55fa92d38f0a00206a000a08ea-2d92c4d5fa92cdd30a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "PDIVision"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class RLEVel(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:RLEVel
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/65c5b3a27d46498f.htm#ID_21e8c0b9fa92db300a00206a01c11504-3791a074fa92d5740a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "RLEVel"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class RPOSition(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:RPOSition
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ea8a750914d84285.htm#ID_1784a4a9fa92e2c20a00206a00192d65-a6fd3b12fa92dd150a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "RPOSition"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class TOP(SCPINode, SCPIQuery, SCPISet):
                            """
                            `DISPlay:WINDow:TRACe:Y:SCALe:TOP
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6331132d7bf24ded.htm#ID_2e553fc3fa92ea630a00206a014ba5b8-4b3a4019fa92e4b60a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "TOP"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                class ZOOM(SCPINode, SCPIBool):
                    """
                    DISPlay:WINDow:TRACe:ZOOM
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "ZOOM"
                    args = ["1", "OFF", "ON"]
                    
                    class BOTTom(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:ZOOM:BOTTom
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8f33192c7c374678.htm#ID_4c13e8946c07013b0a00206a005313ce-15625ccf6c06fa750a00206a01eade93-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "BOTTom"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class STARt(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:ZOOM:STARt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b2b9e703a45644b4.htm#ID_f621ce186c070a050a00206a00e386d0-b4028b3f6c0703bc0a00206a01eade93-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STARt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class STATe(SCPINode, SCPIBool):
                        """
                        `DISPlay:WINDow:TRACe:ZOOM:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/45c943218b544691.htm#ID_0801ee0a6c0728e80a00206a018f38c0-c5604fde6c0721180a00206a01eade93-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                    class STOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:ZOOM:STOP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b2b9e703a45644b4.htm#ID_3ce8f2656c0713d90a00206a010a19da-9ba5e7346c070cb50a00206a01eade93-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STOP"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class TOP(SCPINode, SCPIQuery, SCPISet):
                        """
                        `DISPlay:WINDow:TRACe:ZOOM:TOP
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8f33192c7c374678.htm#ID_537535906c071e680a00206a01dff876-ecb2878b6c0716880a00206a01eade93-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "TOP"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
    class FORMat(SCPINode, SCPIQuery, SCPISet):
        """
        FORMat
        
        Arguments: ASCii, REAL
        """
        _cmd = "FORMat"
        args = ["ASCii", "REAL"]
        
        class BORDer(SCPINode, SCPIQuery, SCPISet):
            """
            `FORMat:BORDer
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e91448.htm#ID_3675bceefa92f1f40a00206a0080e1b0-61996525fa92ec470a00206a01a6673d-en-US>`_
            
            Arguments: NORMal, SWAPped
            """
            _cmd = "BORDer"
            args = ["NORMal", "SWAPped"]
            
        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            `FORMat:DATA
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e91478.htm#ID_42b1c1edfa9301c30a00206a005a835f-27d15adffa92fc260a00206a01a6673d-en-US>`_
            
            Arguments: ASCii, REAL
            """
            _cmd = "DATA"
            args = ["ASCii", "REAL"]
            
        class DEXPort(SCPINode):
            """
            FORMat:DEXPort
            
            Arguments: 
            """
            _cmd = "DEXPort"
            args = [""]
            
            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `FORMat:DEXPort:SOURce
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a4122895a8614cd4.htm#ID_fc4eaae1fa92fa320a00206a008b9cce-81da4c17fa92f3d90a00206a01a6673d-en-US>`_
                
                Arguments: FDATa, MDATa, SDATa
                """
                _cmd = "SOURce"
                args = ["FDATa", "MDATa", "SDATa"]
                
    class HCOPy(SCPINode, SCPISet):
        """
        HCOPy
        
        Arguments: 
        """
        _cmd = "HCOPy"
        args = [""]
        
        class DESTination(SCPINode, SCPIQuery, SCPISet):
            """
            `HCOPy:DESTination
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e91566.htm#ID_4d99c38afa9309840a00206a01d41aa4-cb1d3d15fa9303a80a00206a01a6673d-en-US>`_
            
            Arguments: 'string'
            """
            _cmd = "DESTination"
            args = ["'string'"]
            
        class DEVice(SCPINode):
            """
            HCOPy:DEVice
            
            Arguments: 
            """
            _cmd = "DEVice"
            args = [""]
            
            class LANGuage(SCPINode, SCPIQuery, SCPISet):
                """
                `HCOPy:DEVice:LANGuage
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e91619.htm#ID_bd2a6c37fa9311150a00206a01b42ce6-ccf29715fa930b680a00206a01a6673d-en-US>`_
                
                Arguments: BMP, EMF, EWMF, JPG, PDF, PNG, SVG, WMF
                """
                _cmd = "LANGuage"
                args = ["BMP", "EMF", "EWMF", "JPG", "PDF", "PNG", "SVG", "WMF"]
                
        class IMMediate(SCPINode, SCPISet):
            """
            `HCOPy:IMMediate
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e92039.htm#ID_d21a6a5ffa9365110a00206a01870b2a-5d6c01cbfa935f640a00206a01a6673d-en-US>`_
            
            Arguments: 
            """
            _cmd = "IMMediate"
            args = [""]
            
        class ITEM(SCPINode):
            """
            HCOPy:ITEM
            
            Arguments: 
            """
            _cmd = "ITEM"
            args = [""]
            
            class ALL(SCPINode, SCPISet):
                """
                `HCOPy:ITEM:ALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e91673.htm#ID_94da1e3bfa9318c60a00206a00ef3e34-3800e316fa9312ea0a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "ALL"
                args = [""]
                
            class LOGO(SCPINode, SCPIBool):
                """
                HCOPy:ITEM:LOGO
                
                Arguments: 1, OFF, ON
                """
                _cmd = "LOGO"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `HCOPy:ITEM:LOGO:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e91704.htm#ID_ac9df7a7fa9320860a00206a00ec5c45-4c4a58fcfa931a9b0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class MLISt(SCPINode, SCPIBool):
                """
                HCOPy:ITEM:MLISt
                
                Arguments: 1, OFF, ON
                """
                _cmd = "MLISt"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `HCOPy:ITEM:MLISt:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e91742.htm#ID_854db6e1fa9328370a00206a01529a20-c066e67cfa93227a0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class TIME(SCPINode, SCPIBool):
                """
                HCOPy:ITEM:TIME
                
                Arguments: 1, OFF, ON
                """
                _cmd = "TIME"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `HCOPy:ITEM:TIME:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e91774.htm#ID_83e3f4d2fa932f9a0a00206a010f0f4e-404ea32bfa932a0c0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
        class PAGE(SCPINode):
            """
            HCOPy:PAGE
            
            Arguments: 
            """
            _cmd = "PAGE"
            args = [""]
            
            class COLor(SCPINode, SCPIBool):
                """
                `HCOPy:PAGE:COLor
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e91806.htm#ID_5105d1a3134de2840a00206a0114a6f3-dca49ae8134ddcc80a00206a0182dc26-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "COLor"
                args = ["1", "OFF", "ON"]
                
            class MARGin(SCPINode):
                """
                HCOPy:PAGE:MARGin
                
                Arguments: 
                """
                _cmd = "MARGin"
                args = [""]
                
                class BOTTom(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:BOTTom
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e91842.htm#ID_3dea753bfa93372b0a00206a01c0ca2d-3f62fe82fa93317e0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "BOTTom"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class LEFT(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:LEFT
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e91873.htm#ID_8992c875fa933ebc0a00206a00922775-5c119a03fa93390f0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "LEFT"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class RIGHt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:RIGHt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e91903.htm#ID_c7f0b442fa93465e0a00206a008d1d63-960d34d5fa9340b00a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "RIGHt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class TOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    `HCOPy:PAGE:MARGin:TOP
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e91933.htm#ID_6228e4b0fa934def0a00206a0086d622-cebe271bfa9348520a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "TOP"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class ORIentation(SCPINode, SCPIQuery, SCPISet):
                """
                `HCOPy:PAGE:ORIentation
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e91963.htm#ID_f7b8f767fa9355a00a00206a00c03771-29a7b9bafa934fe30a00206a01a6673d-en-US>`_
                
                Arguments: LANDscape, PORTrait
                """
                _cmd = "ORIentation"
                args = ["LANDscape", "PORTrait"]
                
            class WINDow(SCPINode, SCPIQuery, SCPISet):
                """
                `HCOPy:PAGE:WINDow
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e7101f963f5c4de3.htm#ID_1c0c843ffa935d7f0a00206a015039a1-42f22e75fa9357840a00206a01a6673d-en-US>`_
                
                Arguments: ACTive, ALL, HARDcopy, NONE, SINGle
                """
                _cmd = "WINDow"
                args = ["ACTive", "ALL", "HARDcopy", "NONE", "SINGle"]
                
    class INITiate(SCPINodeN, SCPISet):
        """
        INITiate
        
        Arguments: 
        """
        _cmd = "INITiate"
        args = [""]
        
        class CONTinuous(SCPINode, SCPIBool):
            """
            `INITiate:CONTinuous
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2529407b6dba4f2e.htm#ID_a44b9c33fa936d000a00206a00766e71-d44acbdafa9367050a00206a01a6673d-en-US>`_
            
            Arguments: 1, OFF, ON
            """
            _cmd = "CONTinuous"
            args = ["1", "OFF", "ON"]
            
            class ALL(SCPINode, SCPIBool):
                """
                `INITiate:CONTinuous:ALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e92158.htm#ID_6387403cd8d5523c0a00206a01023265-128b12f9d8d54b860a00206a0133a7b4-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "ALL"
                args = ["1", "OFF", "ON"]
                
        class IMMediate(SCPINode, SCPISet):
            """
            INITiate:IMMediate
            
            Arguments: 
            """
            _cmd = "IMMediate"
            args = [""]
            
            class ALL(SCPINode, SCPISet):
                """
                `INITiate:IMMediate:ALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e92199.htm#ID_912c0160d8d55d770a00206a01491fbe-eddf9798d8d555d60a00206a0133a7b4-en-US>`_
                
                Arguments: 
                """
                _cmd = "ALL"
                args = [""]
                
            class DUMMy(SCPINode, SCPISet):
                """
                `INITiate:IMMediate:DUMMy
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f79d0e51f1b440c9.htm#ID_8a697b81fa937c230a00206a01ed43fb-be0448b2fa9376660a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "DUMMy"
                args = [""]
                
            class SCOPe(SCPINode, SCPIQuery, SCPISet):
                """
                `INITiate:IMMediate:SCOPe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d961912528a64003.htm#ID_0b426df9fa9374820a00206a00380abe-581c1051fa936ef40a00206a01a6673d-en-US>`_
                
                Arguments: ALL, SINGle
                """
                _cmd = "SCOPe"
                args = ["ALL", "SINGle"]
                
    class INPut(SCPINodeN):
        """
        INPut
        
        Arguments: 
        """
        _cmd = "INPut"
        args = [""]
        
        class ATTenuation(SCPINode, SCPIQuery, SCPISet):
            """
            `INPut:ATTenuation
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7f41ca301ecf4a76.htm#ID_cec36677fa9383e30a00206a01063b02-23f6f3d6fa937e070a00206a01a6673d-en-US>`_
            
            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "ATTenuation"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
            
    class INSTrument(SCPINode, SCPIQuery, SCPISet):
        """
        INSTrument
        
        Arguments: CHANnel1, CHANnel2, CHANnel3, CHANnel4
        """
        _cmd = "INSTrument"
        args = ["CHANnel1", "CHANnel2", "CHANnel3", "CHANnel4"]
        
        class NSELect(SCPINode, SCPIQuery, SCPISet):
            """
            `INSTrument:NSELect
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e92362.htm#ID_078f22a7fa938ba40a00206a0072b3e0-af650a43fa9385d70a00206a01a6673d-en-US>`_
            
            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "NSELect"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
            
        class PORT(SCPINode):
            """
            INSTrument:PORT
            
            Arguments: 
            """
            _cmd = "PORT"
            args = [""]
            
            class COUNt(SCPINode, SCPIQuery):
                """
                `INSTrument:PORT:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e92399.htm#ID_9eb542a9fa9393a30a00206a01fd78a5-0f241535fa938d880a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "COUNt"
                args = [""]
                
        class SELect(SCPINode, SCPIQuery, SCPISet):
            """
            `INSTrument:SELect
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e124461.htm#ID_49cfdf62fa939b440a00206a013fc5ae-d0c31584fa9395870a00206a01a6673d-en-US>`_
            
            Arguments: CHANnel1, CHANnel2, CHANnel3, CHANnel4
            """
            _cmd = "SELect"
            args = ["CHANnel1", "CHANnel2", "CHANnel3", "CHANnel4"]
            
        class SMATrix(SCPINode, SCPIBool):
            """
            `INSTrument:SMATrix
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6cf81becf1d94292.htm#ID_c20108e4e2b32f990a002019011edfae-c2391792e2b32e510a002019017b841c-en-US>`_
            
            Arguments: 1, OFF, ON
            """
            _cmd = "SMATrix"
            args = ["1", "OFF", "ON"]
            
        class TPORt(SCPINode):
            """
            INSTrument:TPORt
            
            Arguments: 
            """
            _cmd = "TPORt"
            args = [""]
            
            class COUNt(SCPINode, SCPIQuery):
                """
                `INSTrument:TPORt:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dffa886d18c44be6.htm#ID_a3c1b1d2e2b3316e0a00201901e88744-2e35c5e3e2b330060a002019017b841c-en-US>`_
                
                Arguments: 
                """
                _cmd = "COUNt"
                args = [""]
                
    class MEMory(SCPINode):
        """
        MEMory
        
        Arguments: 
        """
        _cmd = "MEMory"
        args = [""]
        
        class CATalog(SCPINode, SCPIQuery):
            """
            `MEMory:CATalog
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e92484.htm#ID_952acba6fa93a2a60a00206a00158e32-18081993fa939d180a00206a01a6673d-en-US>`_
            
            Arguments: 
            """
            _cmd = "CATalog"
            args = [""]
            
            class COUNt(SCPINode, SCPIQuery):
                """
                `MEMory:CATalog:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/24d4e6c36b6941d1.htm#ID_0562f2d34f2f3f8f0a001ae74fc3b6bb-a8d8bf024f2f3dd90a001ae7211c9327-en-US>`_
                
                Arguments: 
                """
                _cmd = "COUNt"
                args = [""]
                
        class DEFine(SCPINode, SCPISet):
            """
            `MEMory:DEFine
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e92524.htm#ID_061ba650fa93aa180a00206a00c6cfff-c04a3e9ffa93a48b0a00206a01a6673d-en-US>`_
            
            Arguments: 'string'
            """
            _cmd = "DEFine"
            args = ["'string'"]
            
        class DELete(SCPINode, SCPISet):
            """
            MEMory:DELete
            
            Arguments: 'string'
            """
            _cmd = "DELete"
            args = ["'string'"]
            
            class ALL(SCPINode, SCPISet):
                """
                `MEMory:DELete:ALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e92554.htm#ID_35efca29fa93b18b0a00206a00349680-421059c6fa93abfd0a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "ALL"
                args = [""]
                
            class NAME(SCPINode, SCPISet):
                """
                `MEMory:DELete:NAME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e92572.htm#ID_a4188fedfa93b8fd0a00206a007bbe38-13217951fa93b36f0a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "NAME"
                args = ["'string'"]
                
        class SELect(SCPINode, SCPIQuery, SCPISet):
            """
            `MEMory:SELect
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6b5a13422595410a.htm#ID_346e954ffa93c0600a00206a00f12f17-1813a310fa93bae10a00206a01a6673d-en-US>`_
            
            Arguments: 'string'
            """
            _cmd = "SELect"
            args = ["'string'"]
            
    class MMEMory(SCPINode):
        """
        MMEMory
        
        Arguments: 
        """
        _cmd = "MMEMory"
        args = [""]
        
        class AKAL(SCPINode):
            """
            MMEMory:AKAL
            
            Arguments: 
            """
            _cmd = "AKAL"
            args = [""]
            
            class FACTory(SCPINode):
                """
                MMEMory:AKAL:FACTory
                
                Arguments: 
                """
                _cmd = "FACTory"
                args = [""]
                
                class CONVersion(SCPINode, SCPISet):
                    """
                    `MMEMory:AKAL:FACTory:CONVersion
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e92733.htm#ID_00f3bd41fa93c7f10a00206a01f83ace-1386d072fa93c2440a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "CONVersion"
                    args = ["'string'"]
                    
            class USER(SCPINode):
                """
                MMEMory:AKAL:USER
                
                Arguments: 
                """
                _cmd = "USER"
                args = [""]
                
                class CONVersion(SCPINode, SCPISet):
                    """
                    `MMEMory:AKAL:USER:CONVersion
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e92765.htm#ID_0bfad8be134e0c050a00206a0178239a-ada6c16a134e06490a00206a0182dc26-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "CONVersion"
                    args = ["'string'"]
                    
        class CATalog(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:CATalog
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7f7650b75a604b3d.htm#ID_d67d6ebffa93cf820a00206a01a6fbab-84db8dd3fa93c9c60a00206a01a6673d-en-US>`_
            
            Arguments: 'string'
            """
            _cmd = "CATalog"
            args = ["'string'"]
            
            class ALL(SCPINode, SCPIQuery, SCPISet):
                """
                `MMEMory:CATalog:ALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/29a34569412140a3.htm#ID_6bb263ddfa93d6f50a00206a01b648d1-d7bba71dfa93d1670a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "ALL"
                args = ["'string'"]
                
        class CDIRectory(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:CDIRectory
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e92972.htm#ID_a851e04afa93deb50a00206a01ba773c-866493dbfa93d8f80a00206a01a6673d-en-US>`_
            
            Arguments: DEFault, 'string'
            """
            _cmd = "CDIRectory"
            args = ["DEFault", "'string'"]
            
        class CKIT(SCPINode):
            """
            MMEMory:CKIT
            
            Arguments: 
            """
            _cmd = "CKIT"
            args = [""]
            
            class INFO(SCPINode, SCPIQuery, SCPISet):
                """
                `MMEMory:CKIT:INFO
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f05fc8cc8da8453b.htm#ID_977b912c842e29060a00201900b846e9-70e4c8b0842e27320a00201901936165-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "INFO"
                args = ["'string'"]
                
        class COPY(SCPINode, SCPISet):
            """
            `MMEMory:COPY
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e93010.htm#ID_5982002afa93e6270a00206a00a5825e-91ceacf0fa93e08a0a00206a01a6673d-en-US>`_
            
            Arguments: 'string'
            """
            _cmd = "COPY"
            args = ["'string'"]
            
        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:DATA
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e93118.htm#ID_b272d43dfa93eda90a00206a004c602f-6ae124d7fa93e80c0a00206a01a6673d-en-US>`_
            
            Arguments: 'string'
            """
            _cmd = "DATA"
            args = ["'string'"]
            
        class DELete(SCPINode, SCPISet):
            """
            `MMEMory:DELete
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e93164.htm#ID_4f6d0f68fa93f5690a00206a00977265-306d4498fa93efad0a00206a01a6673d-en-US>`_
            
            Arguments: 'string'
            """
            _cmd = "DELete"
            args = ["'string'"]
            
            class CORRection(SCPINode, SCPISet):
                """
                `MMEMory:DELete:CORRection
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e93211.htm#ID_f4141b0cfa93fceb0a00206a015c2d71-9c1f0333fa93f74e0a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "CORRection"
                args = ["'string'"]
                
        class FAVorite(SCPINodeN, SCPIQuery, SCPISet):
            """
            `MMEMory:FAVorite
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cda53011c4e5403d.htm#ID_b9c4d46242aef73c0a001ae75af528d0-f607fbd242aef5670a001ae769a5b4da-en-US>`_
            
            Arguments: 'string'
            """
            _cmd = "FAVorite"
            args = ["'string'"]
            
        class LOAD(SCPINode, SCPISet):
            """
            MMEMory:LOAD
            
            Arguments: 'string'
            """
            _cmd = "LOAD"
            args = ["'string'"]
            
            class CKIT(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:CKIT
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e93318.htm#ID_c78e3dc3fa940c6c0a00206a01f47c9b-d1fd8855fa9406a00a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "CKIT"
                args = ["'string'"]
                
                class SDATa(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CKIT:SDATa
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4fe03fc744814dcd.htm#ID_c1f39b85fa9413de0a00206a01268a9f-3cd2e2d6fa940e410a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "SDATa"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPISet):
                        """
                        `MMEMory:LOAD:CKIT:SDATa:WLABel
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/765abd9f32e14000.htm#ID_05b1f69a066b76e20a001ae73aa0f2d0-7609eb53066b753c0a001ae733608be0-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                class UDIRectory(SCPINode, SCPIQuery, SCPISet):
                    """
                    `MMEMory:LOAD:CKIT:UDIRectory
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e93654.htm#ID_3825c580fa941b7f0a00206a014d2f58-aa68faf7fa9415b30a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "UDIRectory"
                    args = ["'string'"]
                    
            class CMAP(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:CMAP
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e93712.htm#ID_351cf3d6fa9422f20a00206a018d97ca-e2d6eb23fa941d540a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "CMAP"
                args = ["'string'"]
                
            class CORRection(SCPINode, SCPIQuery, SCPISet):
                """
                `MMEMory:LOAD:CORRection
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e93766.htm#ID_25d6c84ffa942a830a00206a0004052a-3d57daf0fa9424c60a00206a01a6673d-en-US>`_
                
                Arguments: 1, ALL, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CORRection"
                args = ["1", "ALL", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class MERGe(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CORRection:MERGe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4de4620d64e54bea.htm#ID_5fb89cc06c078fbf0a00206a00cc1f27-48b5ed616c0787820a00206a01eade93-en-US>`_
                    
                    Arguments: 1, ALL, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "MERGe"
                    args = ["1", "ALL", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class RESolve(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CORRection:RESolve
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e93933.htm#ID_e782fc7bfa9431f50a00206a01e86316-b5f1ce83fa942c580a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, ALL, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "RESolve"
                    args = ["1", "ALL", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class TCOefficient(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:CORRection:TCOefficient
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3391883fd0444077.htm#ID_160bbf146127a73d0a00206a0132199c-5dc6592961279f9c0a00206a01ed2866-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "TCOefficient"
                    args = ["'string'"]
                    
            class EYE(SCPINode):
                """
                MMEMory:LOAD:EYE
                
                Arguments: 
                """
                _cmd = "EYE"
                args = [""]
                
                class BPATtern(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:EYE:BPATtern
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b3feb82126144ee8.htm#ID_d243f9a988f49b750a001ae72a347e86-16a9dbc488f49a0e0a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "BPATtern"
                    args = ["'string'"]
                    
                class JITTer(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:EYE:JITTer
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3a6db511c0d74ac2.htm#ID_bd651b9e88f49f8c0a001ae768b6972e-5ce472ed88f49d980a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "JITTer"
                    args = ["'string'"]
                    
                class MASK(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:EYE:MASK
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/30a568fd0b7a4832.htm#ID_0e3256ff88f4a1710a001ae75ab581a7-1d6fd32e88f4a0480a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "MASK"
                    args = ["'string'"]
                    
            class LIMit(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:LIMit
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8105ab89421143c4.htm#ID_2de53f9cfa9439870a00206a01216055-e1a5d1b6fa9433da0a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "LIMit"
                args = ["'string'"]
                
            class MDAData(SCPINode, SCPISet):
                """
                MMEMory:LOAD:MDAData
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "MDAData"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class MDCData(SCPINode, SCPISet):
                """
                MMEMory:LOAD:MDCData
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "MDCData"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class RIPPle(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:RIPPle
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e94362.htm#ID_53d05c7afa9457fc0a00206a0134102b-a6dd69cffa94523f0a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "RIPPle"
                args = ["'string'"]
                
            class SEGMent(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:SEGMent
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e94421.htm#ID_1bff4bd6fa94bde90a00206a01c2ce76-065d4235fa94b7fd0a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "SEGMent"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class STATe(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7dda8a2a220446bf.htm#ID_98d61c75fa94c54c0a00206a003ae40a-d3527128fa94bfcd0a00206a01a6673d-en-US>`_
                
                Arguments: 1
                """
                _cmd = "STATe"
                args = ["1"]
                
            class TRACe(SCPINode, SCPISet):
                """
                `MMEMory:LOAD:TRACe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e94531.htm#ID_71cd29a3fa94ccdd0a00206a00176ef8-c8a94a32fa94c7300a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "TRACe"
                args = ["'string'"]
                
                class AUTO(SCPINode, SCPISet):
                    """
                    `MMEMory:LOAD:TRACe:AUTO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/19157a43e4c140cf.htm#ID_1129c438581269d50a001ae77ff8a3b6-a64b95bd5812685e0a001ae75f9ff217-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "AUTO"
                    args = ["'string'"]
                    
            class VNETworks(SCPINodeN):
                """
                MMEMory:LOAD:VNETworks
                
                Arguments: 
                """
                _cmd = "VNETworks"
                args = [""]
                
                class BALanced(SCPINode):
                    """
                    MMEMory:LOAD:VNETworks:BALanced
                    
                    Arguments: 
                    """
                    _cmd = "BALanced"
                    args = [""]
                    
                    class DEEMbedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:BALanced:DEEMbedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/68d4179e5b9a4864.htm#ID_60f70d22fa94d4bd0a00206a01d5316a-546be1b0fa94ceb20a00206a01a6673d-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "DEEMbedding"
                        args = ["'string'"]
                        
                    class EMBedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:BALanced:EMBedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f6b1b692bb9b47c5.htm#ID_1fb5e13dfa94dc2f0a00206a017b5ae4-afca2f18fa94d6a10a00206a01a6673d-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "EMBedding"
                        args = ["'string'"]
                        
                class DIFFerential(SCPINode):
                    """
                    MMEMory:LOAD:VNETworks:DIFFerential
                    
                    Arguments: 
                    """
                    _cmd = "DIFFerential"
                    args = [""]
                    
                    class EMBedding(SCPINodeN, SCPISet):
                        """
                        MMEMory:LOAD:VNETworks:DIFFerential:EMBedding
                        
                        Arguments: 'string'
                        """
                        _cmd = "EMBedding"
                        args = ["'string'"]
                        
                class GLOop(SCPINode):
                    """
                    MMEMory:LOAD:VNETworks:GLOop
                    
                    Arguments: 
                    """
                    _cmd = "GLOop"
                    args = [""]
                    
                    class DEEMbedding(SCPINode, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:GLOop:DEEMbedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b4a3d6fa5ec24c48.htm#ID_90df2d0efa94e3c00a00206a00b81c60-551f17abfa94de130a00206a01a6673d-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "DEEMbedding"
                        args = ["'string'"]
                        
                    class EMBedding(SCPINode, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:GLOop:EMBedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3d2e435406c14d5c.htm#ID_6cf57b55fa94eb520a00206a01f0b35d-3002adcbfa94e5a50a00206a01a6673d-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "EMBedding"
                        args = ["'string'"]
                        
                class PPAir(SCPINode):
                    """
                    MMEMory:LOAD:VNETworks:PPAir
                    
                    Arguments: 
                    """
                    _cmd = "PPAir"
                    args = [""]
                    
                    class DEEMbedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:PPAir:DEEMbedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2cc34fe146bb4b3e.htm#ID_0d54645258126fb10a001ae7686ffa62-2155715958126e1a0a001ae75f9ff217-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "DEEMbedding"
                        args = ["'string'"]
                        
                    class EMBedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:PPAir:EMBedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/806ed1787e384089.htm#ID_e33cac3b581272310a001ae769d4469b-f2244cfe5812709b0a001ae75f9ff217-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "EMBedding"
                        args = ["'string'"]
                        
                class SENDed(SCPINode):
                    """
                    MMEMory:LOAD:VNETworks:SENDed
                    
                    Arguments: 
                    """
                    _cmd = "SENDed"
                    args = [""]
                    
                    class DEEMbedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:SENDed:DEEMbedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b4ab11f6c2d1486d.htm#ID_3dd89c63fa94f2d40a00206a00c9b7ad-74a2471cfa94ed360a00206a01a6673d-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "DEEMbedding"
                        args = ["'string'"]
                        
                    class EMBedding(SCPINodeN, SCPISet):
                        """
                        `MMEMory:LOAD:VNETworks:SENDed:EMBedding
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/535bed379ed64bb9.htm#ID_b61e5784fa94fa360a00206a01c80b0f-f1e321c8fa94f4a80a00206a01a6673d-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "EMBedding"
                        args = ["'string'"]
                        
        class MDIRectory(SCPINode, SCPISet):
            """
            `MMEMory:MDIRectory
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e95510.htm#ID_fd35f1fcfa9501b80a00206a0100c42b-88ece1edfa94fc0b0a00206a01a6673d-en-US>`_
            
            Arguments: 'string'
            """
            _cmd = "MDIRectory"
            args = ["'string'"]
            
        class MOVE(SCPINode, SCPISet):
            """
            `MMEMory:MOVE
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e95554.htm#ID_5a4f49b8fa95092a0a00206a01f9980a-904752d9fa95038d0a00206a01a6673d-en-US>`_
            
            Arguments: 'string'
            """
            _cmd = "MOVE"
            args = ["'string'"]
            
        class MSIS(SCPINode, SCPIQuery, SCPISet):
            """
            MMEMory:MSIS
            
            Arguments: 'string'
            """
            _cmd = "MSIS"
            args = ["'string'"]
            
        class NAME(SCPINode, SCPIQuery, SCPISet):
            """
            `MMEMory:NAME
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e95601.htm#ID_7ed3f8e1fa95183e0a00206a018c947f-39b72916fa9512810a00206a01a6673d-en-US>`_
            
            Arguments: 'string'
            """
            _cmd = "NAME"
            args = ["'string'"]
            
        class RDIRectory(SCPINode, SCPISet):
            """
            `MMEMory:RDIRectory
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e95668.htm#ID_13316b07fa951fdf0a00206a008fc1f6-bf8fd2b9fa951a220a00206a01a6673d-en-US>`_
            
            Arguments: 'string'
            """
            _cmd = "RDIRectory"
            args = ["'string'"]
            
        class STORe(SCPINode):
            """
            MMEMory:STORe
            
            Arguments: 
            """
            _cmd = "STORe"
            args = [""]
            
            class CKIT(SCPINode, SCPISet):
                """
                `MMEMory:STORe:CKIT
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e95695.htm#ID_539cfe2efa9527410a00206a01d2a4ac-dd207886fa9521b40a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "CKIT"
                args = ["'string'"]
                
                class WLABel(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:CKIT:WLABel
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/efd3c02d66084bdd.htm#ID_888d60aaced4f53a0a00201901d73653-9c37fbc3ced4f3a40a0020190170f726-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "WLABel"
                    args = ["'string'"]
                    
            class CMAP(SCPINode, SCPISet):
                """
                `MMEMory:STORe:CMAP
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e95808.htm#ID_cbd50bdafa952f400a00206a00ec799b-eab4a1d4fa9529260a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "CMAP"
                args = ["'string'"]
                
            class CORRection(SCPINode, SCPISet):
                """
                `MMEMory:STORe:CORRection
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e95844.htm#ID_c353e6ebfa9536b20a00206a01588c09-64171fb4fa9531150a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CORRection"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class TCOefficient(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:CORRection:TCOefficient
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e95896.htm#ID_9ae3f47f6127dd220a00206a00f0280f-08ed84676127d39c0a00206a01ed2866-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "TCOefficient"
                    args = ["'string'"]
                    
            class EYE(SCPINode):
                """
                MMEMory:STORe:EYE
                
                Arguments: 
                """
                _cmd = "EYE"
                args = [""]
                
                class MASK(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:EYE:MASK
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/94f770900bd1416f.htm#ID_45d1dade88f4ac000a001ae76425c73a-1ce7cc5588f4ab250a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "MASK"
                    args = ["'string'"]
                    
                    class RESults(SCPINode, SCPISet):
                        """
                        `MMEMory:STORe:EYE:MASK:RESults
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/26f174954ce54290.htm#ID_37aa2ebc88f4ad960a001ae724036915-1cfb19f688f4acbb0a001ae77b2dc49c-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "RESults"
                        args = ["'string'"]
                        
                class MEASurements(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:EYE:MEASurements
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8dc577a61b154526.htm#ID_d3e3117988f4af1d0a001ae70b423eef-bdf3e20788f4ae320a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "MEASurements"
                    args = ["'string'"]
                    
            class LIMit(SCPINode, SCPISet):
                """
                `MMEMory:STORe:LIMit
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e96093.htm#ID_782b2ad6fa953e250a00206a019dc625-b89a0a63fa9538870a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "LIMit"
                args = ["'string'"]
                
            class MARKer(SCPINode, SCPISet):
                """
                `MMEMory:STORe:MARKer
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f70a03bc15d4437f.htm#ID_3fc7f68bfa9545c60a00206a00581ca5-eb6af3e4fa9540090a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "MARKer"
                args = ["'string'"]
                
            class MDCData(SCPINode, SCPISet):
                """
                MMEMory:STORe:MDCData
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "MDCData"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class RIPPle(SCPINode, SCPISet):
                """
                `MMEMory:STORe:RIPPle
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e96190.htm#ID_f13d0426fa955c6b0a00206a0012a7ed-6e6fe2c3fa9556bd0a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "RIPPle"
                args = ["'string'"]
                
            class SEGMent(SCPINode, SCPISet):
                """
                `MMEMory:STORe:SEGMent
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e96239.htm#ID_de67ac75fa95640c0a00206a0143d61b-7b9796ebfa955e3f0a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "SEGMent"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class STATe(SCPINode, SCPISet):
                """
                `MMEMory:STORe:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5052a11828174526.htm#ID_905ac710fa956bad0a00206a0007bfeb-0c7b3364fa9566000a00206a01a6673d-en-US>`_
                
                Arguments: 1
                """
                _cmd = "STATe"
                args = ["1"]
                
            class TRACe(SCPINode, SCPISet):
                """
                `MMEMory:STORe:TRACe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a65bbed6ba0147dc.htm#ID_4cefccb1fa95732f0a00206a000ff211-d0689586fa956d820a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "TRACe"
                args = ["'string'"]
                
                class CHANnel(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:TRACe:CHANnel
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e96477.htm#ID_5e3f64c9fa957aa10a00206a0151de90-1d6679b9fa9575030a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, ALL, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "CHANnel"
                    args = ["1", "ALL", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class OPTion(SCPINode):
                    """
                    MMEMory:STORe:TRACe:OPTion
                    
                    Arguments: 
                    """
                    _cmd = "OPTion"
                    args = [""]
                    
                    class PLUS(SCPINode, SCPIQuery, SCPISet):
                        """
                        `MMEMory:STORe:TRACe:OPTion:PLUS
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ff40aa0133194ed1.htm#ID_b9900453a1e9a3150a001ae76280abec-a8ea7a81a1e9a1be0a001ae70a9caa95-en-US>`_
                        
                        Arguments: PLUS, SPACe, VOID
                        """
                        _cmd = "PLUS"
                        args = ["PLUS", "SPACe", "VOID"]
                        
                    class SSEParator(SCPINode, SCPIBool):
                        """
                        `MMEMory:STORe:TRACe:OPTion:SSEParator
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a565459101494c2b.htm#ID_5f64ab6ca1e9a4bb0a001ae77a2699fa-13ddc4d6a1e9a3920a001ae70a9caa95-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "SSEParator"
                        args = ["1", "OFF", "ON"]
                        
                    class TABS(SCPINode, SCPIBool):
                        """
                        `MMEMory:STORe:TRACe:OPTion:TABS
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cc452c005766424d.htm#ID_fd30ef37a1e9a6710a001ae756b484ff-1daf23f2a1e9a5480a001ae70a9caa95-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "TABS"
                        args = ["1", "OFF", "ON"]
                        
                    class TRIM(SCPINode, SCPIBool):
                        """
                        `MMEMory:STORe:TRACe:OPTion:TRIM
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/83a697c6e4ad47f1.htm#ID_6b425a6ba1e9a8170a001ae778e72705-0e2fc535a1e9a6ee0a001ae70a9caa95-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "TRIM"
                        args = ["1", "OFF", "ON"]
                        
                class PORTs(SCPINode, SCPISet):
                    """
                    `MMEMory:STORe:TRACe:PORTs
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bf349758d8b24668.htm#ID_39dd05bffa9582320a00206a01a97190-b9b34189fa957c850a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, 'string', COMPlex, LINPhase, LOGPhase, CIMPedance, PIMPedance
                    """
                    _cmd = "PORTs"
                    args = ["1", "'string'", "COMPlex", "LINPhase", "LOGPhase", "CIMPedance", "PIMPedance"]
                    
    class OUTPut(SCPINodeN, SCPIBool):
        """
        OUTPut
        
        Arguments: 1, OFF, ON
        """
        _cmd = "OUTPut"
        args = ["1", "OFF", "ON"]
        
        class DPORt(SCPINode, SCPIQuery, SCPISet):
            """
            `OUTPut:DPORt
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0c0cec1ef82643e1.htm#ID_917ab5bffa95a7bc0a00206a01b0fd26-0934dcfcfa95a1ff0a00206a01a6673d-en-US>`_
            
            Arguments: PORT1, PORT2, PORT3, PORT4
            """
            _cmd = "DPORt"
            args = ["PORT1", "PORT2", "PORT3", "PORT4"]
            
        class STATe(SCPINode, SCPIBool):
            """
            `OUTPut:STATe
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5bef3747737e49a1.htm#ID_1d3950befa95a01a0a00206a004f6799-85cf6e20fa959a7d0a00206a01a6673d-en-US>`_
            
            Arguments: 1, OFF, ON
            """
            _cmd = "STATe"
            args = ["1", "OFF", "ON"]
            
        class UPORt(SCPINode, SCPIQuery):
            """
            OUTPut:UPORt
            
            Arguments: 
            """
            _cmd = "UPORt"
            args = [""]
            
            class ECBits(SCPINode, SCPIBool):
                """
                `OUTPut:UPORt:ECBits
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e96868.htm#ID_954978c2134e5c960a00206a00bd7009-5e1d0c11134e56e90a00206a0182dc26-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "ECBits"
                args = ["1", "OFF", "ON"]
                
            class SEGMent(SCPINodeN, SCPIQuery):
                """
                OUTPut:UPORt:SEGMent
                
                Arguments: 
                """
                _cmd = "SEGMent"
                args = [""]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    OUTPut:UPORt:SEGMent:STATe
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
                class VALue(SCPINode, SCPIQuery):
                    """
                    OUTPut:UPORt:SEGMent:VALue
                    
                    Arguments: 
                    """
                    _cmd = "VALue"
                    args = [""]
                    
            class VALue(SCPINode, SCPIQuery):
                """
                `OUTPut:UPORt:VALue
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e1e93d03a7df427c.htm#ID_135223a3fa9598a80a00206a01cafb20-52630dd2fa95931a0a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "VALue"
                args = [""]
                
    class PROGram(SCPINode):
        """
        PROGram
        
        Arguments: 
        """
        _cmd = "PROGram"
        args = [""]
        
        class SELected(SCPINode):
            """
            PROGram:SELected
            
            Arguments: 
            """
            _cmd = "SELected"
            args = [""]
            
            class EXECute(SCPINode, SCPISet):
                """
                `PROGram:SELected:EXECute
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/392c9cb1d1974b06.htm#ID_189c3c21fa95b6ee0a00206a00783ab2-c1c63606fa95b1310a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "EXECute"
                args = ["'string'"]
                
            class INIMessage(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:INIMessage
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e97220.htm#ID_40e3620ffa95bfa80a00206a008f8ff5-31d51170fa95ba0b0a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "INIMessage"
                args = ["'string'"]
                
            class INIParameter(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:INIParameter
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e97336.htm#ID_7a6b9636fa95c73a0a00206a00d1a901-d14937334d3699ed0a00206a01f0cf39-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "INIParameter"
                args = ["'string'"]
                
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:NAME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e97030.htm#ID_c54cbe36fa95cebc0a00206a00f8e5b9-e2ad44defa95c91e0a00206a01a6673d-en-US>`_
                
                Arguments: PROG
                """
                _cmd = "NAME"
                args = ["PROG"]
                
            class RETVal(SCPINode, SCPIQuery):
                """
                `PROGram:SELected:RETVal
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/02fc3f1a6eaf42d6.htm#ID_94731fde6f66e3560a001ae73692d158-f209efbd6f66e1b00a001ae727f5f310-en-US>`_
                
                Arguments: 
                """
                _cmd = "RETVal"
                args = [""]
                
            class WAIT(SCPINode, SCPIQuery, SCPISet):
                """
                `PROGram:SELected:WAIT
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/82b54e96d1e44f4f.htm#ID_6029b303fa95de0e0a00206a01d08fa1-a92a19e1fa95d8410a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "WAIT"
                args = [""]
                
    class SENSe(SCPINodeN):
        """
        SENSe
        
        Arguments: 
        """
        _cmd = "SENSe"
        args = [""]
        
        class AVERage(SCPINode, SCPIBool):
            """
            SENSe:AVERage
            
            Arguments: 1, OFF, ON
            """
            _cmd = "AVERage"
            args = ["1", "OFF", "ON"]
            
            class CLEar(SCPINode, SCPISet):
                """
                `SENSe:AVERage:CLEar
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ff10e010f00d4b14.htm#ID_f98b8f87fa95f4f10a00206a01537005-1a87cdf1fa95ef340a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "CLEar"
                args = [""]
                
            class COUNt(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:AVERage:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5f171177edec4acc.htm#ID_60175c19fa95fc920a00206a018e0d61-0ec39e5bfa95f6d50a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "COUNt"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:AVERage:MODE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b22adeaf572d4a3a.htm#ID_bb3fe278aaa7f2390a00206a00c5463f-a0adc45baaa7e6240a00206a00dee6b8-en-US>`_
                
                Arguments: AUTO, FLATten, MOVing, REDuce
                """
                _cmd = "MODE"
                args = ["AUTO", "FLATten", "MOVing", "REDuce"]
                
            class STATe(SCPINode, SCPIBool):
                """
                `SENSe:AVERage:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f2c90c7855f6416e.htm#ID_befa63f5fa9604240a00206a019d1b7a-b4429b00fa95fe760a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
        class BANDwidth(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:BANDwidth
            
            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "BANDwidth"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
            
            class RESolution(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:BANDwidth:RESolution
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dd1fd694e0ce4dd8.htm#ID_97a679d7fa960b960a00206a00572e56-c5d81c23fa9606080a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "RESolution"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:BANDwidth:RESolution:SELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5bf234a092e54a5c.htm#ID_ac511438fa9613080a00206a00a13823-54b75391fa960d6a0a00206a01a6673d-en-US>`_
                    
                    Arguments: HIGH, MEDium, NORMal
                    """
                    _cmd = "SELect"
                    args = ["HIGH", "MEDium", "NORMal"]
                    
        class BWIDth(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:BWIDth
            
            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "BWIDth"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
            
            class RESolution(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:BWIDth:RESolution
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dd1fd694e0ce4dd8.htm#ID_3a4684e0fa961ad80a00206a013fb6ed-0a999090fa9614ec0a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "RESolution"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:BWIDth:RESolution:SELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5bf234a092e54a5c.htm#ID_ba204243fa96223b0a00206a007de2b3-d020815dfa961cad0a00206a01a6673d-en-US>`_
                    
                    Arguments: HIGH, MEDium, NORMal
                    """
                    _cmd = "SELect"
                    args = ["HIGH", "MEDium", "NORMal"]
                    
        class CORRection(SCPINode, SCPIBool):
            """
            SENSe:CORRection
            
            Arguments: 1, OFF, ON
            """
            _cmd = "CORRection"
            args = ["1", "OFF", "ON"]
            
            class CDATa(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:CDATa
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/56c4604324f74fdd.htm#ID_61872ddefa962a0b0a00206a00f647f7-3f3fd3eafa96245d0a00206a01a6673d-en-US>`_
                
                Arguments: 1, 'string'
                """
                _cmd = "CDATa"
                args = ["1", "'string'"]
                
                class CATalog(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CDATa:CATalog
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "CATalog"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class PORT(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CDATa:PORT
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/56c4604324f74fdd.htm#ID_1d57879f3512ffaa0a00206a00fd361c-e90129e83512f8570a00206a01f2dc17-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "PORT"
                    args = ["'string'"]
                    
                    class CATalog(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CDATa:PORT:CATalog
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "CATalog"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
            class CKIT(SCPINode):
                """
                SENSe:CORRection:CKIT
                
                Arguments: 
                """
                _cmd = "CKIT"
                args = [""]
                
                class CATalog(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:CATalog
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/20ee7245586f47ab.htm#ID_275e8b37fa96319c0a00206a00b96b39-8b99fd8cfa962bef0a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "CATalog"
                    args = ["'string'"]
                    
                class DELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:DELete
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e98824.htm#ID_d581a0a8fa96390e0a00206a0093c656-0318d330fa9633710a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "DELete"
                    args = ["'string'"]
                    
                class DMODe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:DMODe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b0b16acb033e4002.htm#ID_3d0e560697e8eb360a001ae7274e8676-670d0e8997e8e99f0a001ae760f7f904-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "DMODe"
                    args = ["'string'"]
                    
                class FFATten(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FFATten
                    
                    Arguments: 'string'
                    """
                    _cmd = "FFATten"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FFATten:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FFATten:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FFLine
                    
                    Arguments: 'string'
                    """
                    _cmd = "FFLine"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FFLine:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FFLine:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FFSNetwork
                    
                    Arguments: 'string'
                    """
                    _cmd = "FFSNetwork"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FFSNetwork:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FFSNetwork:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FFTHrough
                    
                    Arguments: 'string'
                    """
                    _cmd = "FFTHrough"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FFTHrough:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FFTHrough:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class FMTCh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FMTCh
                    
                    Arguments: 'string'
                    """
                    _cmd = "FMTCh"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FMTCh:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FMTCh:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class FOPen(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FOPen
                    
                    Arguments: 'string'
                    """
                    _cmd = "FOPen"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FOPen:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FOPen:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class FOSHort(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FOSHort
                    
                    Arguments: 'string'
                    """
                    _cmd = "FOSHort"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FOSHort:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FOSHort:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class FREFlect(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FREFlect
                    
                    Arguments: 'string'
                    """
                    _cmd = "FREFlect"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FREFlect:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FREFlect:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class FSHort(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FSHort
                    
                    Arguments: 'string'
                    """
                    _cmd = "FSHort"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FSHort:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FSHort:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class FSMatch(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:FSMatch
                    
                    Arguments: 'string'
                    """
                    _cmd = "FSMatch"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:FSMatch:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:FSMatch:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class INSTall(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:INSTall
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e124693.htm#ID_0d28ed7afa968ceb0a00206a00c14d10-2f7f204bfa96872e0a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "INSTall"
                    args = ["'string'"]
                    
                class LABel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LABel
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/468d3061fddc4522.htm#ID_a949aef5fa96949b0a00206a008cfdb4-08f09b7dfa968ecf0a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "LABel"
                    args = ["'string'"]
                    
                class LCATalog(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LCATalog
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6e82c490f7f24b6b.htm#ID_bd9285fcced51a760a0020190106d279-9543f45cced5191e0a0020190170f726-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "LCATalog"
                    args = ["'string'"]
                    
                class LDELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LDELete
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e95eefb5eb454112.htm#ID_8cfb4403ced51c5a0a002019000160a1-3112cb6eced51af30a0020190170f726-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "LDELete"
                    args = ["'string'"]
                    
                class LLABel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LLABel
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/436dc8aef9bf4100.htm#ID_4ee989a8ced51e2f0a00201900885604-edc77a82ced51ce70a0020190170f726-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "LLABel"
                    args = ["'string'"]
                    
                class LSELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:LSELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/538cff17731d484f.htm#ID_16b73472ced51fe50a002019002e86ba-dbeec92aced51eac0a0020190170f726-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "LSELect"
                    args = ["'string'"]
                    
                class MFATten(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MFATten
                    
                    Arguments: 'string'
                    """
                    _cmd = "MFATten"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MFATten:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MFATten:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MFLine
                    
                    Arguments: 'string'
                    """
                    _cmd = "MFLine"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MFLine:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MFLine:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MFSNetwork
                    
                    Arguments: 'string'
                    """
                    _cmd = "MFSNetwork"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MFSNetwork:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MFSNetwork:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MFTHrough
                    
                    Arguments: 'string'
                    """
                    _cmd = "MFTHrough"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MFTHrough:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MFTHrough:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class MMATten(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMATten
                    
                    Arguments: 'string'
                    """
                    _cmd = "MMATten"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMATten:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MMATten:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMLine
                    
                    Arguments: 'string'
                    """
                    _cmd = "MMLine"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMLine:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MMLine:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMSNetwork
                    
                    Arguments: 'string'
                    """
                    _cmd = "MMSNetwork"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMSNetwork:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MMSNetwork:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class MMTCh(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMTCh
                    
                    Arguments: 'string'
                    """
                    _cmd = "MMTCh"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMTCh:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MMTCh:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MMTHrough
                    
                    Arguments: 'string'
                    """
                    _cmd = "MMTHrough"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MMTHrough:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MMTHrough:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class MOPen(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MOPen
                    
                    Arguments: 'string'
                    """
                    _cmd = "MOPen"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MOPen:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MOPen:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class MOSHort(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MOSHort
                    
                    Arguments: 'string'
                    """
                    _cmd = "MOSHort"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MOSHort:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MOSHort:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class MREFlect(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MREFlect
                    
                    Arguments: 'string'
                    """
                    _cmd = "MREFlect"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MREFlect:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MREFlect:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class MSHort(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MSHort
                    
                    Arguments: 'string'
                    """
                    _cmd = "MSHort"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MSHort:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MSHort:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class MSMatch(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:MSMatch
                    
                    Arguments: 'string'
                    """
                    _cmd = "MSMatch"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:MSMatch:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:MSMatch:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class N(SCPINodeN):
                    """
                    SENSe:CORRection:CKIT:N
                    
                    Arguments: 
                    """
                    _cmd = "N"
                    args = [""]
                    
                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FFATten
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFATten"
                        args = ["'string'"]
                        
                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FFLine
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFLine"
                        args = ["'string'"]
                        
                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FFSNetwork
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFSNetwork"
                        args = ["'string'"]
                        
                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FFTHrough
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFTHrough"
                        args = ["'string'"]
                        
                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FMTCh
                        
                        Arguments: 'string'
                        """
                        _cmd = "FMTCh"
                        args = ["'string'"]
                        
                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FOPen
                        
                        Arguments: 'string'
                        """
                        _cmd = "FOPen"
                        args = ["'string'"]
                        
                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FREFlect
                        
                        Arguments: 'string'
                        """
                        _cmd = "FREFlect"
                        args = ["'string'"]
                        
                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FSHort
                        
                        Arguments: 'string'
                        """
                        _cmd = "FSHort"
                        args = ["'string'"]
                        
                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:FSMatch
                        
                        Arguments: 'string'
                        """
                        _cmd = "FSMatch"
                        args = ["'string'"]
                        
                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:LSELect
                        
                        Arguments: 'string'
                        """
                        _cmd = "LSELect"
                        args = ["'string'"]
                        
                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MFATten
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFATten"
                        args = ["'string'"]
                        
                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MFLine
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFLine"
                        args = ["'string'"]
                        
                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MFSNetwork
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFSNetwork"
                        args = ["'string'"]
                        
                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MFTHrough
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFTHrough"
                        args = ["'string'"]
                        
                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMATten
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMATten"
                        args = ["'string'"]
                        
                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMLine
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMLine"
                        args = ["'string'"]
                        
                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMSNetwork
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMSNetwork"
                        args = ["'string'"]
                        
                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMTCh
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMTCh"
                        args = ["'string'"]
                        
                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MMTHrough
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMTHrough"
                        args = ["'string'"]
                        
                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MOPen
                        
                        Arguments: 'string'
                        """
                        _cmd = "MOPen"
                        args = ["'string'"]
                        
                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MREFlect
                        
                        Arguments: 'string'
                        """
                        _cmd = "MREFlect"
                        args = ["'string'"]
                        
                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MSHort
                        
                        Arguments: 'string'
                        """
                        _cmd = "MSHort"
                        args = ["'string'"]
                        
                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:MSMatch
                        
                        Arguments: 'string'
                        """
                        _cmd = "MSMatch"
                        args = ["'string'"]
                        
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:N:SELect
                        
                        Arguments: 'string'
                        """
                        _cmd = "SELect"
                        args = ["'string'"]
                        
                class OSHort(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CKIT:OSHort
                    
                    Arguments: 'string'
                    """
                    _cmd = "OSHort"
                    args = ["'string'"]
                    
                    class WLABel(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:OSHort:WLABel
                        
                        Arguments: 'string'
                        """
                        _cmd = "WLABel"
                        args = ["'string'"]
                        
                        class SDATa(SCPINode, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:CKIT:OSHort:WLABel:SDATa
                            
                            Arguments: 'string'
                            """
                            _cmd = "SDATa"
                            args = ["'string'"]
                            
                class PC(SCPINodeN):
                    """
                    SENSe:CORRection:CKIT:PC
                    
                    Arguments: 
                    """
                    _cmd = "PC"
                    args = [""]
                    
                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FFATten
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFATten"
                        args = ["'string'"]
                        
                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FFLine
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFLine"
                        args = ["'string'"]
                        
                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FFSNetwork
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFSNetwork"
                        args = ["'string'"]
                        
                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FFTHrough
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFTHrough"
                        args = ["'string'"]
                        
                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FMTCh
                        
                        Arguments: 'string'
                        """
                        _cmd = "FMTCh"
                        args = ["'string'"]
                        
                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FOPen
                        
                        Arguments: 'string'
                        """
                        _cmd = "FOPen"
                        args = ["'string'"]
                        
                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FREFlect
                        
                        Arguments: 'string'
                        """
                        _cmd = "FREFlect"
                        args = ["'string'"]
                        
                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FSHort
                        
                        Arguments: 'string'
                        """
                        _cmd = "FSHort"
                        args = ["'string'"]
                        
                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:FSMatch
                        
                        Arguments: 'string'
                        """
                        _cmd = "FSMatch"
                        args = ["'string'"]
                        
                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:LSELect
                        
                        Arguments: 'string'
                        """
                        _cmd = "LSELect"
                        args = ["'string'"]
                        
                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MFATten
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFATten"
                        args = ["'string'"]
                        
                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MFLine
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFLine"
                        args = ["'string'"]
                        
                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MFSNetwork
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFSNetwork"
                        args = ["'string'"]
                        
                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MFTHrough
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFTHrough"
                        args = ["'string'"]
                        
                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMATten
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMATten"
                        args = ["'string'"]
                        
                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMLine
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMLine"
                        args = ["'string'"]
                        
                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMSNetwork
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMSNetwork"
                        args = ["'string'"]
                        
                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMTCh
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMTCh"
                        args = ["'string'"]
                        
                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MMTHrough
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMTHrough"
                        args = ["'string'"]
                        
                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MOPen
                        
                        Arguments: 'string'
                        """
                        _cmd = "MOPen"
                        args = ["'string'"]
                        
                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MREFlect
                        
                        Arguments: 'string'
                        """
                        _cmd = "MREFlect"
                        args = ["'string'"]
                        
                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MSHort
                        
                        Arguments: 'string'
                        """
                        _cmd = "MSHort"
                        args = ["'string'"]
                        
                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:MSMatch
                        
                        Arguments: 'string'
                        """
                        _cmd = "MSMatch"
                        args = ["'string'"]
                        
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:PC:SELect
                        
                        Arguments: 'string'
                        """
                        _cmd = "SELect"
                        args = ["'string'"]
                        
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:CKIT:SELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e99073.htm#ID_b65e4b76fa9a70630a00206a0107a5c6-69af0339fa9a6aa60a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "SELect"
                    args = ["'string'"]
                    
                class SMA(SCPINode):
                    """
                    SENSe:CORRection:CKIT:SMA
                    
                    Arguments: 
                    """
                    _cmd = "SMA"
                    args = [""]
                    
                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FFATten
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFATten"
                        args = ["'string'"]
                        
                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FFLine
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFLine"
                        args = ["'string'"]
                        
                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FFSNetwork
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFSNetwork"
                        args = ["'string'"]
                        
                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FFTHrough
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFTHrough"
                        args = ["'string'"]
                        
                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FMTCh
                        
                        Arguments: 'string'
                        """
                        _cmd = "FMTCh"
                        args = ["'string'"]
                        
                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FOPen
                        
                        Arguments: 'string'
                        """
                        _cmd = "FOPen"
                        args = ["'string'"]
                        
                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FREFlect
                        
                        Arguments: 'string'
                        """
                        _cmd = "FREFlect"
                        args = ["'string'"]
                        
                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FSHort
                        
                        Arguments: 'string'
                        """
                        _cmd = "FSHort"
                        args = ["'string'"]
                        
                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:FSMatch
                        
                        Arguments: 'string'
                        """
                        _cmd = "FSMatch"
                        args = ["'string'"]
                        
                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:LSELect
                        
                        Arguments: 'string'
                        """
                        _cmd = "LSELect"
                        args = ["'string'"]
                        
                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MFATten
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFATten"
                        args = ["'string'"]
                        
                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MFLine
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFLine"
                        args = ["'string'"]
                        
                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MFSNetwork
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFSNetwork"
                        args = ["'string'"]
                        
                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MFTHrough
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFTHrough"
                        args = ["'string'"]
                        
                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMATten
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMATten"
                        args = ["'string'"]
                        
                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMLine
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMLine"
                        args = ["'string'"]
                        
                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMSNetwork
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMSNetwork"
                        args = ["'string'"]
                        
                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMTCh
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMTCh"
                        args = ["'string'"]
                        
                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MMTHrough
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMTHrough"
                        args = ["'string'"]
                        
                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MOPen
                        
                        Arguments: 'string'
                        """
                        _cmd = "MOPen"
                        args = ["'string'"]
                        
                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MREFlect
                        
                        Arguments: 'string'
                        """
                        _cmd = "MREFlect"
                        args = ["'string'"]
                        
                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MSHort
                        
                        Arguments: 'string'
                        """
                        _cmd = "MSHort"
                        args = ["'string'"]
                        
                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:MSMatch
                        
                        Arguments: 'string'
                        """
                        _cmd = "MSMatch"
                        args = ["'string'"]
                        
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:SMA:SELect
                        
                        Arguments: 'string'
                        """
                        _cmd = "SELect"
                        args = ["'string'"]
                        
                class STANdard(SCPINode):
                    """
                    SENSe:CORRection:CKIT:STANdard
                    
                    Arguments: 
                    """
                    _cmd = "STANdard"
                    args = [""]
                    
                    class CATalog(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:CKIT:STANdard:CATalog
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/173aa73feb9f4da4.htm#ID_0c560487fa9b35f50a00206a018f09d5-04e887fdfa9b2fab0a00206a01a6673d-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "CATalog"
                        args = ["'string'"]
                        
                    class DATA(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:CKIT:STANdard:DATA
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6ed615a6cfde42d5.htm#ID_f9688ab997e995bf0a001ae742db5fd2-d35c0fa897e994970a001ae760f7f904-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "DATA"
                        args = ["'string'"]
                        
                    class LCATalog(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:CKIT:STANdard:LCATalog
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3c29f476a1cb4a51.htm#ID_ef4a7ad2ced55c710a0020190114b7a4-6db5736aced55b390a0020190170f726-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "LCATalog"
                        args = ["'string'"]
                        
                class USER(SCPINodeN):
                    """
                    SENSe:CORRection:CKIT:USER
                    
                    Arguments: 
                    """
                    _cmd = "USER"
                    args = [""]
                    
                    class FFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FFATten
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFATten"
                        args = ["'string'"]
                        
                    class FFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FFLine
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFLine"
                        args = ["'string'"]
                        
                    class FFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FFSNetwork
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFSNetwork"
                        args = ["'string'"]
                        
                    class FFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FFTHrough
                        
                        Arguments: 'string'
                        """
                        _cmd = "FFTHrough"
                        args = ["'string'"]
                        
                    class FMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FMTCh
                        
                        Arguments: 'string'
                        """
                        _cmd = "FMTCh"
                        args = ["'string'"]
                        
                    class FOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FOPen
                        
                        Arguments: 'string'
                        """
                        _cmd = "FOPen"
                        args = ["'string'"]
                        
                    class FOSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FOSHort
                        
                        Arguments: 'string'
                        """
                        _cmd = "FOSHort"
                        args = ["'string'"]
                        
                    class FREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FREFlect
                        
                        Arguments: 'string'
                        """
                        _cmd = "FREFlect"
                        args = ["'string'"]
                        
                    class FSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FSHort
                        
                        Arguments: 'string'
                        """
                        _cmd = "FSHort"
                        args = ["'string'"]
                        
                    class FSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:FSMatch
                        
                        Arguments: 'string'
                        """
                        _cmd = "FSMatch"
                        args = ["'string'"]
                        
                    class LSELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:LSELect
                        
                        Arguments: 'string'
                        """
                        _cmd = "LSELect"
                        args = ["'string'"]
                        
                    class MFATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MFATten
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFATten"
                        args = ["'string'"]
                        
                    class MFLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MFLine
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFLine"
                        args = ["'string'"]
                        
                    class MFSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MFSNetwork
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFSNetwork"
                        args = ["'string'"]
                        
                    class MFTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MFTHrough
                        
                        Arguments: 'string'
                        """
                        _cmd = "MFTHrough"
                        args = ["'string'"]
                        
                    class MMATten(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMATten
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMATten"
                        args = ["'string'"]
                        
                    class MMLine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMLine
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMLine"
                        args = ["'string'"]
                        
                    class MMSNetwork(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMSNetwork
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMSNetwork"
                        args = ["'string'"]
                        
                    class MMTCh(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMTCh
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMTCh"
                        args = ["'string'"]
                        
                    class MMTHrough(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MMTHrough
                        
                        Arguments: 'string'
                        """
                        _cmd = "MMTHrough"
                        args = ["'string'"]
                        
                    class MOPen(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MOPen
                        
                        Arguments: 'string'
                        """
                        _cmd = "MOPen"
                        args = ["'string'"]
                        
                    class MOSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MOSHort
                        
                        Arguments: 'string'
                        """
                        _cmd = "MOSHort"
                        args = ["'string'"]
                        
                    class MREFlect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MREFlect
                        
                        Arguments: 'string'
                        """
                        _cmd = "MREFlect"
                        args = ["'string'"]
                        
                    class MSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MSHort
                        
                        Arguments: 'string'
                        """
                        _cmd = "MSHort"
                        args = ["'string'"]
                        
                    class MSMatch(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:MSMatch
                        
                        Arguments: 'string'
                        """
                        _cmd = "MSMatch"
                        args = ["'string'"]
                        
                    class OSHort(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:OSHort
                        
                        Arguments: 'string'
                        """
                        _cmd = "OSHort"
                        args = ["'string'"]
                        
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:CKIT:USER:SELect
                        
                        Arguments: 'string'
                        """
                        _cmd = "SELect"
                        args = ["'string'"]
                        
            class COLLect(SCPINode, SCPISet):
                """
                SENSe:CORRection:COLLect
                
                Arguments: ATT, IMATch12, LINe1, LINe2, LINe3, M1O2, M1S2, MATCh1, MATCh12, MATCh2, NET, O1M2, OPEN1, OPEN12, OPEN2, OSHort1, OSHort11, OSHort12, OSHort13, OSHort2, OSHort21, OSHort22, OSHort23, REFL1, REFL2, S1M2, SHORt1, SHORt12, SHORt2, SLIDe1, SLIDe12, SLIDe2, THRough, UTHRough
                """
                _cmd = "COLLect"
                args = ["ATT", "IMATch12", "LINe1", "LINe2", "LINe3", "M1O2", "M1S2", "MATCh1", "MATCh12", "MATCh2", "NET", "O1M2", "OPEN1", "OPEN12", "OPEN2", "OSHort1", "OSHort11", "OSHort12", "OSHort13", "OSHort2", "OSHort21", "OSHort22", "OSHort23", "REFL1", "REFL2", "S1M2", "SHORt1", "SHORt12", "SHORt2", "SLIDe1", "SLIDe12", "SLIDe2", "THRough", "UTHRough"]
                
                class ACQuire(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5bae4485a66a4fdb.htm#ID_ef5ce226fa9d34b10a00206a00b1eeba-d8380b43fa9d2ed50a00206a01a6673d-en-US>`_
                    
                    Arguments: ATT, IMATch12, LINe1, LINe2, LINe3, M1O2, M1S2, MATCh1, MATCh12, MATCh2, NET, O1M2, OPEN1, OPEN12, OPEN2, OSHort1, OSHort11, OSHort12, OSHort13, OSHort2, OSHort21, OSHort22, OSHort23, REFL1, REFL2, S1M2, SHORt1, SHORt12, SHORt2, SLIDe1, SLIDe12, SLIDe2, THRough, UTHRough
                    """
                    _cmd = "ACQuire"
                    args = ["ATT", "IMATch12", "LINe1", "LINe2", "LINe3", "M1O2", "M1S2", "MATCh1", "MATCh12", "MATCh2", "NET", "O1M2", "OPEN1", "OPEN12", "OPEN2", "OSHort1", "OSHort11", "OSHort12", "OSHort13", "OSHort2", "OSHort21", "OSHort22", "OSHort23", "REFL1", "REFL2", "S1M2", "SHORt1", "SHORt12", "SHORt2", "SLIDe1", "SLIDe12", "SLIDe2", "THRough", "UTHRough"]
                    
                    class RSAVe(SCPINode, SCPIBool):
                        """
                        SENSe:CORRection:COLLect:ACQuire:RSAVe
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "RSAVe"
                        args = ["1", "OFF", "ON"]
                        
                        class DEFault(SCPINode, SCPIBool):
                            """
                            SENSe:CORRection:COLLect:ACQuire:RSAVe:DEFault
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "DEFault"
                            args = ["1", "OFF", "ON"]
                            
                    class SELected(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:ACQuire:SELected
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c6919bbe1b864cae.htm#ID_c00a21defa9d4bc30a00206a0122a8dd-5adea6c9fa9d46260a00206a01a6673d-en-US>`_
                        
                        Arguments: ATT, ISOLation, LINE, LINe1, LINe2, LINe3, MATCh, NET, OPEN, OSHort, OSHort1, OSHort2, OSHort3, POWer, REFL, SHORt, SLIDe, THRough, UTHRough
                        """
                        _cmd = "SELected"
                        args = ["ATT", "ISOLation", "LINE", "LINe1", "LINe2", "LINe3", "MATCh", "NET", "OPEN", "OSHort", "OSHort1", "OSHort2", "OSHort3", "POWer", "REFL", "SHORt", "SLIDe", "THRough", "UTHRough"]
                        
                class AUTO(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:AUTO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3f0c418e57de4397.htm#ID_cc386375fa9c629c0a00206a00bdf63e-10769a8bfa9c5cd00a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "AUTO"
                    args = ["'string'"]
                    
                    class ASSignment(SCPINodeN):
                        """
                        SENSe:CORRection:COLLect:AUTO:ASSignment
                        
                        Arguments: 
                        """
                        _cmd = "ASSignment"
                        args = [""]
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:ASSignment:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c1af194ea15e4e74.htm#ID_5df4176ee2b44c640a002019017f4ab1-12b12dc3e2b44b0c0a002019017b841c-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "ACQuire"
                            args = [""]
                            
                        class ALL(SCPINode):
                            """
                            SENSe:CORRection:COLLect:AUTO:ASSignment:ALL
                            
                            Arguments: 
                            """
                            _cmd = "ALL"
                            args = [""]
                            
                            class COUNt(SCPINode, SCPIQuery):
                                """
                                `SENSe:CORRection:COLLect:AUTO:ASSignment:ALL:COUNt
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d48b52bc242b4e32.htm#ID_959263675de614120a002019017e262e-dd26319f5de612c90a0020190152315a-en-US>`_
                                
                                Arguments: 
                                """
                                _cmd = "COUNt"
                                args = [""]
                                
                        class COUNt(SCPINode, SCPIQuery):
                            """
                            `SENSe:CORRection:COLLect:AUTO:ASSignment:COUNt
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/18fc2beb38824da2.htm#ID_741269fee2b44e580a0020190035a217-8ce9a3a7e2b44d000a002019017b841c-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "COUNt"
                            args = [""]
                            
                        class DEFine(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:ASSignment:DEFine
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0b4c577ed7c44274.htm#ID_a4e0bf56e2b4504c0a002019012145a1-ee4aa62fe2b44ee40a002019017b841c-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "DEFine"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                            class DEFault(SCPINode, SCPISet):
                                """
                                `SENSe:CORRection:COLLect:AUTO:ASSignment:DEFine:DEFault
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/64618e3b6c8a48f8.htm#ID_1806c3a7e2b452ec0a002019013da53d-5bf3d390e2b450e80a002019017b841c-en-US>`_
                                
                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "DEFault"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                                
                            class TPORt(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SENSe:CORRection:COLLect:AUTO:ASSignment:DEFine:TPORt
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5e83b118ba4a4af5.htm#ID_fefffc76ac615e840a00201901f142c0-e2627403ac615d3c0a0020190003471b-en-US>`_
                                
                                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                """
                                _cmd = "TPORt"
                                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                                
                                class DEFault(SCPINode, SCPISet):
                                    """
                                    `SENSe:CORRection:COLLect:AUTO:ASSignment:DEFine:TPORt:DEFault
                                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ffe7ec78e06d46ea.htm#ID_31e7cb915de618860a002019010fd717-b75dbe175de6175d0a0020190152315a-en-US>`_
                                    
                                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                                    """
                                    _cmd = "DEFault"
                                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                                    
                        class DELete(SCPINode):
                            """
                            SENSe:CORRection:COLLect:AUTO:ASSignment:DELete
                            
                            Arguments: 
                            """
                            _cmd = "DELete"
                            args = [""]
                            
                            class ALL(SCPINode, SCPISet):
                                """
                                `SENSe:CORRection:COLLect:AUTO:ASSignment:DELete:ALL
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/39cbade56c074b32.htm#ID_f5aac7e8e2b4559b0a00201901c4483e-40720b28e2b453970a002019017b841c-en-US>`_
                                
                                Arguments: 
                                """
                                _cmd = "ALL"
                                args = [""]
                                
                    class CKIT(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:CKIT
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9c183d7ea83443b9.htm#ID_53832a46fa9c6a2e0a00206a01a37c63-f7039c7cfa9c64810a00206a01a6673d-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "CKIT"
                        args = ["'string'"]
                        
                        class PASSword(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:CKIT:PASSword
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e100767.htm#ID_2a769be13f255d480a00206a00c9e150-22af427d3f2551130a00206a01f2dc17-en-US>`_
                            
                            Arguments: 'string'
                            """
                            _cmd = "PASSword"
                            args = ["'string'"]
                            
                        class PORTs(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:CKIT:PORTs
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/abf506d433e74aa3.htm#ID_f432d1b6e2b458890a00201900df2894-0415557ee2b456f30a002019017b841c-en-US>`_
                            
                            Arguments: 'string'
                            """
                            _cmd = "PORTs"
                            args = ["'string'"]
                            
                            class ADD(SCPINode, SCPISet):
                                """
                                `SENSe:CORRection:COLLect:AUTO:CKIT:PORTs:ADD
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d3fbc9d3f8b54fa6.htm#ID_22e73eec5de61b450a002019006fdae0-c43eb67b5de61a0d0a0020190152315a-en-US>`_
                                
                                Arguments: 'string'
                                """
                                _cmd = "ADD"
                                args = ["'string'"]
                                
                    class CONFigure(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:CONFigure
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/43d940fc71ac4b9e.htm#ID_ec747919e2b45a4e0a00201900e617f8-1282c43ae2b458e70a002019017b841c-en-US>`_
                        
                        Arguments: FNPort, FOPort, FRTRans, FTRans, OPTPort, PFNPort, REFL, RSHort, RTRans, UTRans
                        """
                        _cmd = "CONFigure"
                        args = ["FNPort", "FOPort", "FRTRans", "FTRans", "OPTPort", "PFNPort", "REFL", "RSHort", "RTRans", "UTRans"]
                        
                    class PORTs(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:PORTs
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/50bac54fa7384143.htm#ID_3691cfa7fa9c71cf0a00206a0106bbfe-1e1e838afa9c6c220a00206a01a6673d-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "PORTs"
                        args = ["'string'"]
                        
                        class CONNection(SCPINode, SCPIQuery):
                            """
                            `SENSe:CORRection:COLLect:AUTO:PORTs:CONNection
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e101087.htm#ID_aaa87597fa9c79700a00206a006071b6-b18811a1fa9c73c30a00206a01a6673d-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "CONNection"
                            args = [""]
                            
                        class TYPE(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:AUTO:PORTs:TYPE
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d551e43da6ab4f79.htm#ID_9ba6f23efa9c81020a00206a012c71ef-cfe00d3cfa9c7b540a00206a01a6673d-en-US>`_
                            
                            Arguments: FNPort, FOPort, FRTRans, FTRans, OPTPort, PFNPort, REFL, RSHort, RTRans, UTRans
                            """
                            _cmd = "TYPE"
                            args = ["FNPort", "FOPort", "FRTRans", "FTRans", "OPTPort", "PFNPort", "REFL", "RSHort", "RTRans", "UTRans"]
                            
                    class POWer(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:POWer
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ece5a47d15bb4f5a.htm#ID_daecab843f258e990a00206a01d8b36c-57484f7f3f25861d0a00206a01f2dc17-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "POWer"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class SAVE(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:SAVE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/df7c981e3a554bbb.htm#ID_b67aa0efe2b45f300a00201900118a61-f6c4fe37e2b45de80a002019017b841c-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "SAVE"
                        args = [""]
                        
                    class TYPE(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:AUTO:TYPE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7483c5a061284b1f.htm#ID_36396a4bfa9c894f0a00206a01b4efbf-b7c40877fa9c82e60a00206a01a6673d-en-US>`_
                        
                        Arguments: FNPort, FOPort, FRTRans, FTRans, OPTPort, PFNPort, REFL, RSHort, RTRans, UTRans
                        """
                        _cmd = "TYPE"
                        args = ["FNPort", "FOPort", "FRTRans", "FTRans", "OPTPort", "PFNPort", "REFL", "RSHort", "RTRans", "UTRans"]
                        
                class AVERage(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:AVERage
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/63d5284950ff4da7.htm#ID_08198f833f0376d20a00201900418d9e-7e26d60a3f03756a0a00201901e91f0b-en-US>`_
                    
                    Arguments: AUTO, MANual
                    """
                    _cmd = "AVERage"
                    args = ["AUTO", "MANual"]
                    
                class CHANnels(SCPINode):
                    """
                    SENSe:CORRection:COLLect:CHANnels
                    
                    Arguments: 
                    """
                    _cmd = "CHANnels"
                    args = [""]
                    
                    class ALL(SCPINode, SCPIBool):
                        """
                        `SENSe:CORRection:COLLect:CHANnels:ALL
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e101434.htm#ID_34af02743512c65b0a00206a00362a14-7b024c7c3512beaa0a00206a01f2dc17-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "ALL"
                        args = ["1", "OFF", "ON"]
                        
                    class MCTYpes(SCPINode, SCPIBool):
                        """
                        `SENSe:CORRection:COLLect:CHANnels:MCTYpes
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a4e2f413400d479a.htm#ID_fb54ec3a42b0257e0a001ae77eed22c3-f1e1839d42b023c90a001ae769a5b4da-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "MCTYpes"
                        args = ["1", "OFF", "ON"]
                        
                class CKIT(SCPINode):
                    """
                    SENSe:CORRection:COLLect:CKIT
                    
                    Arguments: 
                    """
                    _cmd = "CKIT"
                    args = [""]
                    
                    class INSTall(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CKIT:INSTall
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d704124a02f74b82.htm#ID_a4fc6106842e87b10a00201901eee4e7-881b8a8f842e864a0a00201901936165-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "INSTall"
                        args = ["'string'"]
                        
                    class LOAD(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CKIT:LOAD
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/19eb6d332bd148fd.htm#ID_91e2e7bb842e89c40a00201901d9aa95-312cf34c842e883e0a00201901936165-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "LOAD"
                        args = ["'string'"]
                        
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CKIT:PORT
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0383cf4db4d4429e.htm#ID_05b047fd842e8be70a00201901d09b34-d6b0335d842e8a700a00201901936165-en-US>`_
                        
                        Arguments: CONNector, GENDer, LABel, NAME
                        """
                        _cmd = "PORT"
                        args = ["CONNector", "GENDer", "LABel", "NAME"]
                        
                class CONNection(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:CONNection
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/03265a2065d24aa7.htm#ID_51cce608fa9c91bb0a00206a019f3803-81b5f60bfa9c8b910a00206a01a6673d-en-US>`_
                    
                    Arguments: BNC50female, BNC50male, BNC75female, BNC75male, N50Female, N50Male, N75Female, N75Male, PC292female, PC292male, PC35female, PC35male, PC7, SMAFemale, SMAMale, UFEMale1, UFEMale2, UMALe1, UMALe2
                    """
                    _cmd = "CONNection"
                    args = ["BNC50female", "BNC50male", "BNC75female", "BNC75male", "N50Female", "N50Male", "N75Female", "N75Male", "PC292female", "PC292male", "PC35female", "PC35male", "PC7", "SMAFemale", "SMAMale", "UFEMale1", "UFEMale2", "UMALe1", "UMALe2"]
                    
                    class GENDers(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CONNection:GENDers
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c63ca1c037e64fb8.htm#ID_b1dca677135238210a00206a00aaa3a0-d8439156135232640a00206a0182dc26-en-US>`_
                        
                        Arguments: ALL, SINGle
                        """
                        _cmd = "GENDers"
                        args = ["ALL", "SINGle"]
                        
                    class PORTs(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:CONNection:PORTs
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8566df6a31664d76.htm#ID_00065edcfa9c99d90a00206a01564942-32668de0fa9c93af0a00206a01a6673d-en-US>`_
                        
                        Arguments: ALL, SINGle
                        """
                        _cmd = "PORTs"
                        args = ["ALL", "SINGle"]
                        
                class DELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:DELete
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2ad00861f5b34278.htm#ID_1eb59eedfa9ca2070a00206a002812f3-1406a431fa9c9bdc0a00206a01a6673d-en-US>`_
                    
                    Arguments: ALL, 'string'
                    """
                    _cmd = "DELete"
                    args = ["ALL", "'string'"]
                    
                class ERRor(SCPINode, SCPIQuery):
                    """
                    SENSe:CORRection:COLLect:ERRor
                    
                    Arguments: 
                    """
                    _cmd = "ERRor"
                    args = [""]
                    
                class FIXTure(SCPINode, SCPISet):
                    """
                    SENSe:CORRection:COLLect:FIXTure
                    
                    Arguments: OPEN, SHORt
                    """
                    _cmd = "FIXTure"
                    args = ["OPEN", "SHORt"]
                    
                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/baea708b7c254238.htm#ID_c22640a8fa9ccde90a00206a0017e345-5e45eb40fa9cc7320a00206a01a6673d-en-US>`_
                        
                        Arguments: OPEN, SHORt
                        """
                        _cmd = "ACQuire"
                        args = ["OPEN", "SHORt"]
                        
                    class EXPort(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:EXPort
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cdba7a0f9aab4eee.htm#ID_5b2eb4d5a6eab6940a001ae72c53e02a-418808e9a6eab51d0a001ae729ca0bb3-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "EXPort"
                        args = ["'string'"]
                        
                    class IMPort(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:IMPort
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cdba7a0f9aab4eee.htm#ID_c8c75a54a6eab8a80a001ae71f2af99f-b95927ecaae4e1f10a001ae70925c00c-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "IMPort"
                        args = ["'string'"]
                        
                    class LMParameter(SCPINode, SCPIBool):
                        """
                        SENSe:CORRection:COLLect:FIXTure:LMParameter
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "LMParameter"
                        args = ["1", "OFF", "ON"]
                        
                        class LOSS(SCPINode, SCPIBool):
                            """
                            SENSe:CORRection:COLLect:FIXTure:LMParameter:LOSS
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "LOSS"
                            args = ["1", "OFF", "ON"]
                            
                            class STATe(SCPINode, SCPIBool):
                                """
                                `SENSe:CORRection:COLLect:FIXTure:LMParameter:LOSS:STATe
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/60ac72a649b24071.htm#ID_61297150fa9caa440a00206a01dd071f-244481e2fa9ca3fb0a00206a01a6673d-en-US>`_
                                
                                Arguments: 1, OFF, ON
                                """
                                _cmd = "STATe"
                                args = ["1", "OFF", "ON"]
                                
                        class STATe(SCPINode, SCPIBool):
                            """
                            `SENSe:CORRection:COLLect:FIXTure:LMParameter:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/594469a5314f4530.htm#ID_de9f2028fa9cb2fe0a00206a01cb5ae0-84440f34fa9cac480a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                    class SAVE(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:SAVE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f8f30ac030744b53.htm#ID_6eec3f5efa9cbba90a00206a00d4fca3-753af30dfa9cb5210a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "SAVE"
                        args = [""]
                        
                    class STARt(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:FIXTure:STARt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1ed97663b6774143.htm#ID_91250745fa9cc4e00a00206a01bd2953-4cf1ec84fa9cbdeb0a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "STARt"
                        args = [""]
                        
                class LOAD(SCPINode):
                    """
                    SENSe:CORRection:COLLect:LOAD
                    
                    Arguments: 
                    """
                    _cmd = "LOAD"
                    args = [""]
                    
                    class SELected(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:LOAD:SELected
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9494dd1d711a413b.htm#ID_c10b85456c0c5cad0a00206a002bc4d4-6857c5656c0c51cf0a00206a01eade93-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "SELected"
                        args = ["'string'"]
                        
                class METHod(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:METHod
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b70277ab91e94a61.htm#ID_3b1451ddfa9cd6450a00206a0173e35e-f66c5332fa9cd01b0a00206a01a6673d-en-US>`_
                    
                    Arguments: ETOM, ETSM, FOPort1, FOPort12, FOPort2, FOPTport, FRTRans, FTRans, REFL1, REFL12, REFL2, ROPTport, RTRans, TNA, TOM, TOSM, TPORt, TRL, TRM, TSM, UOSM
                    """
                    _cmd = "METHod"
                    args = ["ETOM", "ETSM", "FOPort1", "FOPort12", "FOPort2", "FOPTport", "FRTRans", "FTRans", "REFL1", "REFL12", "REFL2", "ROPTport", "RTRans", "TNA", "TOM", "TOSM", "TPORt", "TRL", "TRM", "TSM", "UOSM"]
                    
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:METHod:DEFine
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/24bc511f46a7483a.htm#ID_aaba0ddffa9cde440a00206a019c590e-74fbf89bfa9cd8490a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, 'string', ETOM, ETSM, FOPort1, FOPort12, FOPort2, FOPTport, FRTRans, FTRans, REFL1, REFL12, REFL2, ROPTport, RTRans, TNA, TOM, TOSM, TPORt, TRL, TRM, TSM, UOSM
                        """
                        _cmd = "DEFine"
                        args = ["1", "'string'", "ETOM", "ETSM", "FOPort1", "FOPort12", "FOPort2", "FOPTport", "FRTRans", "FTRans", "REFL1", "REFL12", "REFL2", "ROPTport", "RTRans", "TNA", "TOM", "TOSM", "TPORt", "TRL", "TRM", "TSM", "UOSM"]
                        
                class PMETer(SCPINode):
                    """
                    SENSe:CORRection:COLLect:PMETer
                    
                    Arguments: 
                    """
                    _cmd = "PMETer"
                    args = [""]
                    
                    class ID(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:PMETer:ID
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e102579.htm#ID_5bda58c53512d2ed0a00206a010922a3-3fb7cfcf3512c9a60a00206a01f2dc17-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "ID"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class SAVE(SCPINode, SCPISet):
                    """
                    SENSe:CORRection:COLLect:SAVE
                    
                    Arguments: 
                    """
                    _cmd = "SAVE"
                    args = [""]
                    
                    class DEFault(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:SAVE:DEFault
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/27cd611c98df422b.htm#ID_29dbd581fa9d097b0a00206a00f2378b-e91b3dc2fa9d03120a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "DEFault"
                        args = [""]
                        
                    class DUMMy(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:COLLect:SAVE:DUMMy
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9578a3d0f68b43f6.htm#ID_ef2c6f57fa9d24650a00206a00bbe1ad-9e8aac18fa9d1d700a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "DUMMy"
                        args = [""]
                        
                    class SELected(SCPINode, SCPISet):
                        """
                        SENSe:CORRection:COLLect:SAVE:SELected
                        
                        Arguments: 
                        """
                        _cmd = "SELected"
                        args = [""]
                        
                        class DEFault(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:SAVE:SELected:DEFault
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d6b4af70d4224ab3.htm#ID_de443b96fa9d11e70a00206a014e80a8-932f4fb4fa9d0b9d0a00206a01a6673d-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "DEFault"
                            args = [""]
                            
                        class DUMMy(SCPINode, SCPISet):
                            """
                            `SENSe:CORRection:COLLect:SAVE:SELected:DUMMy
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1d56c9ae6dcd4805.htm#ID_6e9ab6f4fa9d1b1e0a00206a01a07be4-0f07f7f3fa9d14190a00206a01a6673d-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "DUMMy"
                            args = [""]
                            
                class SCONnection(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:COLLect:SCONnection
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8da8250da50d4831.htm#ID_01899f1efa9d2cc20a00206a00e935a8-c3bdda95fa9d26d60a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "SCONnection"
                    args = ["'string'"]
                    
            class CONNection(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:CONNection
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6a95957e0c09448f.htm#ID_8ce9dfd6fa9d53450a00206a0113cb5f-f8a0ef34fa9d4db70a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "CONNection"
                args = ["'string'"]
                
                class CATalog(SCPINode, SCPIQuery):
                    """
                    `SENSe:CORRection:CONNection:CATalog
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/40aa01430fea4e5e.htm#ID_79a95dcbfa9d5ac70a00206a00e29836-98a422edfa9d55290a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "CATalog"
                    args = [""]
                    
                class DELete(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:CONNection:DELete
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/48ba6caa89804951.htm#ID_395171f4fa9d62490a00206a001360eb-1041e23ffa9d5c9c0a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "DELete"
                    args = ["'string'"]
                    
            class CSET(SCPINode):
                """
                SENSe:CORRection:CSET
                
                Arguments: 
                """
                _cmd = "CSET"
                args = [""]
                
                class DESCription(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:CSET:DESCription
                    
                    Arguments: 'string'
                    """
                    _cmd = "DESCription"
                    args = ["'string'"]
                    
            class DATA(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:DATA
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a4c46fde7af640d1.htm#ID_96ff5d0afa9d718b0a00206a01f3d838-01a15260fa9d6bbf0a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "DATA"
                args = ["'string'"]
                
                class PARameter(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:DATA:PARameter
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/23ded7e07ce64385.htm#ID_f3df74b6fa9d78fd0a00206a01be988b-a95dfeb4fa9d73600a00206a01a6673d-en-US>`_
                    
                    Arguments: ACAL, BANDwidth, CKIT, FSMode, LTSTamp, MTESt, MVNA, PDLY, POINts, PORTs, RATTenuation, SPORt, SPOWer, STARt, STOP, STYPe, THRoughs, TSTamp, TVNA, TYPE
                    """
                    _cmd = "PARameter"
                    args = ["ACAL", "BANDwidth", "CKIT", "FSMode", "LTSTamp", "MTESt", "MVNA", "PDLY", "POINts", "PORTs", "RATTenuation", "SPORt", "SPOWer", "STARt", "STOP", "STYPe", "THRoughs", "TSTamp", "TVNA", "TYPE"]
                    
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SENSe:CORRection:DATA:PARameter:COUNt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d34a1f2a8f994c22.htm#ID_b4b8c587e2b476620a00201900e87abc-cccf6c58e2b475290a002019017b841c-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "COUNt"
                        args = [""]
                        
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:DATA:PARameter:PORT
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/23ded7e07ce64385.htm#ID_59416659351399f60a00206a01efcee1-dcc75689351391a90a00206a01f2dc17-en-US>`_
                        
                        Arguments: ACAL, BANDwidth, CKIT, FSMode, LTSTamp, MTESt, MVNA, PDLY, POINts, PORTs, RATTenuation, SPORt, SPOWer, STARt, STOP, STYPe, THRoughs, TSTamp, TVNA, TYPE
                        """
                        _cmd = "PORT"
                        args = ["ACAL", "BANDwidth", "CKIT", "FSMode", "LTSTamp", "MTESt", "MVNA", "PDLY", "POINts", "PORTs", "RATTenuation", "SPORt", "SPOWer", "STARt", "STOP", "STYPe", "THRoughs", "TSTamp", "TVNA", "TYPE"]
                        
            class DATE(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:DATE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4dd13cde83174c3c.htm#ID_5fc665affa9d806f0a00206a00be0e91-519f73bdfa9d7ae20a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "DATE"
                args = [""]
                
            class DSTate(SCPINode, SCPIQuery):
                """
                SENSe:CORRection:DSTate
                
                Arguments: 
                """
                _cmd = "DSTate"
                args = [""]
                
            class EDELay(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:CORRection:EDELay
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "EDELay"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class AUTO(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:AUTO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c0309a71cecc4d65.htm#ID_086c6faffa9d87e20a00206a009223dc-943616b5fa9d82440a00206a01a6673d-en-US>`_
                    
                    Arguments: ONCE
                    """
                    _cmd = "AUTO"
                    args = ["ONCE"]
                    
                class DIELectric(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:DIELectric
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bfd7289a5fd44070.htm#ID_6ae1e633fa9d8f730a00206a01721163-3f04d6d3fa9d89c60a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DIELectric"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class DISTance(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:DISTance
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b7f8cd6052834f53.htm#ID_70b40f05fa9d96f50a00206a004c7fd4-86ce2b88fa9d91570a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DISTance"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class ELENgth(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:ELENgth
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/157c536c22cf4d9a.htm#ID_640b9ad4fa9d9e670a00206a01bfa35f-8a305bbffa9d98d90a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "ELENgth"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:EDELay:TIME
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e028626ab9d44bf9.htm#ID_ab5a15eefa9da6180a00206a0031b88e-9ce7e9c4fa9da04c0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "TIME"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class LOSS(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:CORRection:LOSS
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2902157d598f48ce.htm#ID_e6e77f94fa9db56a0a00206a0193f03d-33f5f50ffa9daf8e0a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "LOSS"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class AUTO(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:LOSS:AUTO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9c89299de8954e56.htm#ID_a9794b32fa9dbd0b0a00206a00198b3b-88926c88fa9db74e0a00206a01a6673d-en-US>`_
                    
                    Arguments: ONCE
                    """
                    _cmd = "AUTO"
                    args = ["ONCE"]
                    
                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:LOSS:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e17920dcadb14ebe.htm#ID_eaedac34fa9dc48d0a00206a0015b590-244f9ff3fa9dbeef0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "FREQuency"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class OFFSet(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:LOSS:OFFSet
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bcbdd9797a884be7.htm#ID_1b00a820fa9dcc3d0a00206a018802f3-f294d833fa9dc6810a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "OFFSet"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class OFFSet(SCPINodeN, SCPIBool):
                """
                SENSe:CORRection:OFFSet
                
                Arguments: 1, OFF, ON
                """
                _cmd = "OFFSet"
                args = ["1", "OFF", "ON"]
                
                class COMPensation(SCPINode, SCPIBool):
                    """
                    SENSe:CORRection:OFFSet:COMPensation
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "COMPensation"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SENSe:CORRection:OFFSet:COMPensation:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/238a1fddd13747e0.htm#ID_840216d6a6eac4dd0a001ae756bfb09a-f47f6deea6eac3660a001ae729ca0bb3-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class DFComp(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:CORRection:OFFSet:DFComp
                    
                    Arguments: 
                    """
                    _cmd = "DFComp"
                    args = [""]
                    
                    class STATe(SCPINode, SCPIQuery):
                        """
                        `SENSe:CORRection:OFFSet:DFComp:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/586836c972434d7e.htm#ID_df319251fa9ddc3b0a00206a000d80ee-97ada771fa9dd66f0a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "STATe"
                        args = [""]
                        
                class MAGNitude(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:OFFSet:MAGNitude
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1e81fc08465043b6.htm#ID_8f8dc01ffa9de5630a00206a006db9af-424d6ac0fa9ddfa60a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "MAGNitude"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:CORRection:OFFSet:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6485389d1a28497a.htm#ID_5b5ee42bfa9ded040a00206a01bba80c-d2212d06fa9de7470a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class PCAL(SCPINode, SCPISet):
                """
                `SENSe:CORRection:PCAL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f951bfb5b8df44ac.htm#ID_f2fa2fc6aaa800620a00206a0094909c-e54697eeaaa7f46c0a00206a00dee6b8-en-US>`_
                
                Arguments: ALL, NONE
                """
                _cmd = "PCAL"
                args = ["ALL", "NONE"]
                
            class POWer(SCPINodeN, SCPIBool):
                """
                SENSe:CORRection:POWer
                
                Arguments: 1, OFF, ON
                """
                _cmd = "POWer"
                args = ["1", "OFF", "ON"]
                
                class ACQuire(SCPINode, SCPISet):
                    """
                    `SENSe:CORRection:POWer:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/11090299f2ed4cb0.htm#ID_e41508c7fa9df4950a00206a013d8a2a-c4d9f94dfa9deed90a00206a01a6673d-en-US>`_
                    
                    Arguments: AWAVe, B1, B2, B3, B4, BWAVe
                    """
                    _cmd = "ACQuire"
                    args = ["AWAVe", "B1", "B2", "B3", "B4", "BWAVe"]
                    
                class AWAVe(SCPINode, SCPIBool):
                    """
                    SENSe:CORRection:POWer:AWAVe
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "AWAVe"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SENSe:CORRection:POWer:AWAVe:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1066b6f12da342a8.htm#ID_39a8d55efa9dfc360a00206a016597eb-d55487bdfa9df6890a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:POWer:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6920624db9394985.htm#ID_da5741dffa9e04930a00206a01c80d11-15e9d1bffa9dfe2a0a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "DATA"
                    args = ["'string'"]
                    
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:POWer:DATA:PORT
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6920624db9394985.htm#ID_e7e7d1f03513d0d40a00206a019c308c-9a1221113513c9530a00206a01f2dc17-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "PORT"
                        args = ["'string'"]
                        
                class HARMonic(SCPINode):
                    """
                    SENSe:CORRection:POWer:HARMonic
                    
                    Arguments: 
                    """
                    _cmd = "HARMonic"
                    args = [""]
                    
                    class ACQuire(SCPINode, SCPISet):
                        """
                        SENSe:CORRection:POWer:HARMonic:ACQuire
                        
                        Arguments: 
                        """
                        _cmd = "ACQuire"
                        args = [""]
                        
                class IMODulation(SCPINode):
                    """
                    SENSe:CORRection:POWer:IMODulation
                    
                    Arguments: 
                    """
                    _cmd = "IMODulation"
                    args = [""]
                    
                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SENSe:CORRection:POWer:IMODulation:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e0a7ba12dfc644c7.htm#ID_8280b6dffa9e13e50a00206a00dfea28-2ca4e2bafa9e0e280a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "ACQuire"
                        args = [""]
                        
                class MIXer(SCPINode):
                    """
                    SENSe:CORRection:POWer:MIXer
                    
                    Arguments: 
                    """
                    _cmd = "MIXer"
                    args = [""]
                    
                    class IF(SCPINode):
                        """
                        SENSe:CORRection:POWer:MIXer:IF
                        
                        Arguments: 
                        """
                        _cmd = "IF"
                        args = [""]
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            SENSe:CORRection:POWer:MIXer:IF:ACQuire
                            
                            Arguments: 
                            """
                            _cmd = "ACQuire"
                            args = [""]
                            
                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:CORRection:POWer:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7646142b089747f0.htm#ID_45ae6bc1fa9eeadb0a00206a011182c9-b8091dc0fa9ee4f00a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class PSTate(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:PSTate
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cc435717f8b94267.htm#ID_df533854e2b482770a002019006f0182-17cc5a84e2b4813f0a002019017b841c-en-US>`_
                
                Arguments: 
                """
                _cmd = "PSTate"
                args = [""]
                
            class SMATrix(SCPINode):
                """
                SENSe:CORRection:SMATrix
                
                Arguments: 
                """
                _cmd = "SMATrix"
                args = [""]
                
                class CDATa(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:CORRection:SMATrix:CDATa
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/502fca8391fe467f.htm#ID_f5cc70d5e2b4840e0a002019018689c7-265a6a30e2b482d50a002019017b841c-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "CDATa"
                    args = ["'string'"]
                    
                    class CATalog(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SENSe:CORRection:SMATrix:CDATa:CATalog
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "CATalog"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:CORRection:SMATrix:CDATa:PORT
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/502fca8391fe467f.htm#ID_985f5c3ee2b4875a0a00201900ca10d1-4f0b1f65e2b486310a002019017b841c-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "PORT"
                        args = ["'string'"]
                        
                        class CATalog(SCPINodeN, SCPIQuery, SCPISet):
                            """
                            SENSe:CORRection:SMATrix:CDATa:PORT:CATalog
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "CATalog"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
            class SSTate(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:SSTate
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/032f6950568d45b0.htm#ID_ef2640f7fa9ef24e0a00206a0113e683-793bfa23fa9eecc00a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "SSTate"
                args = [""]
                
            class STATe(SCPINode, SCPIBool):
                """
                `SENSe:CORRection:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9e4376c2e66f46fb.htm#ID_1251d801fa9ef9c00a00206a00c826db-8d11769cfa9ef4320a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
            class STIMulus(SCPINode, SCPIQuery):
                """
                `SENSe:CORRection:STIMulus
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7c130eacff3645f3.htm#ID_3870b1b51353668f0a00206a01286f0b-eaf26caa135360e10a00206a0182dc26-en-US>`_
                
                Arguments: 
                """
                _cmd = "STIMulus"
                args = [""]
                
                class PORT(SCPINodeN, SCPIQuery):
                    """
                    `SENSe:CORRection:STIMulus:PORT
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7c130eacff3645f3.htm#ID_aca3f0a13513ea960a00206a007adc1d-2c5c50a33513e3330a00206a01f2dc17-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "PORT"
                    args = [""]
                    
        class COUPle(SCPINode, SCPIQuery, SCPISet):
            """
            `SENSe:COUPle
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6bd6847283104056.htm#ID_b39880affa9f01320a00206a01556890-2f7c24edfa9efba40a00206a01a6673d-en-US>`_
            
            Arguments: ALL, AUTO, NONE
            """
            _cmd = "COUPle"
            args = ["ALL", "AUTO", "NONE"]
            
        class DC(SCPINodeN):
            """
            SENSe:DC
            
            Arguments: 
            """
            _cmd = "DC"
            args = [""]
            
            class RANGe(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:DC:RANGe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/59cff42e06dc4f8e.htm#ID_85e3c36e1356b77d0a00206a0011de08-ec487a421356b1d00a00206a0182dc26-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "RANGe"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
        class FREQuency(SCPINodeN, SCPIQuery, SCPISet):
            """
            SENSe:FREQuency
            
            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "FREQuency"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
            
            class CENTer(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:CENTer
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/42d8825bb9304f5a.htm#ID_e2406746fa9f360d0a00206a00158714-aed43b75fa9f30700a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CENTer"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class CONVersion(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:CONVersion
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c8efca597e3c4cad.htm#ID_a3bb2a00fa9f3d700a00206a01051abd-48ef6c66fa9f37e20a00206a01a6673d-en-US>`_
                
                Arguments: ARBitrary, FUNDamental, HARMonic, MIXer, SHARmonic, THARmonic
                """
                _cmd = "CONVersion"
                args = ["ARBitrary", "FUNDamental", "HARMonic", "MIXer", "SHARmonic", "THARmonic"]
                
                class ARBitrary(SCPINode):
                    """
                    `SENSe:FREQuency:CONVersion:ARBitrary
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e106017.htm#ID_98a8a17bfa9f45010a00206a009ce494-022448048c5dc3830a00206a0022f285-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "ARBitrary"
                    args = [""]
                    
                    class PMETer(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:ARBitrary:PMETer
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/588399e0817144b3.htm#ID_f08d8321fa9f4c640a00206a00cb7453-0eba10acfa9f46e60a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "PMETer"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class GAIN(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:GAIN
                    
                    Arguments: 
                    """
                    _cmd = "GAIN"
                    args = [""]
                    
                    class LMCorrection(SCPINode, SCPIBool):
                        """
                        `SENSe:FREQuency:CONVersion:GAIN:LMCorrection
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ddf6ae7f67c14862.htm#ID_19b501f261299b6a0a00206a013f7404-10d65d59612992af0a00206a01ed2866-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "LMCorrection"
                        args = ["1", "OFF", "ON"]
                        
                class HARMonic(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:HARMonic
                    
                    Arguments: 
                    """
                    _cmd = "HARMonic"
                    args = [""]
                    
                    class ORDer(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:HARMonic:ORDer
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "ORDer"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class RELative(SCPINode, SCPIBool):
                        """
                        SENSe:FREQuency:CONVersion:HARMonic:RELative
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "RELative"
                        args = ["1", "OFF", "ON"]
                        
                    class RPORt(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:HARMonic:RPORt
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "RPORt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class SPORt(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:HARMonic:SPORt
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "SPORt"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class MIXer(SCPINode):
                    """
                    SENSe:FREQuency:CONVersion:MIXer
                    
                    Arguments: 
                    """
                    _cmd = "MIXer"
                    args = [""]
                    
                    class FFIXed(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:MIXer:FFIXed
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "FFIXed"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class FIXed(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:FIXed
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/60891c3d7fd54ed6.htm#ID_4644b954fa9fa0fc0a00206a004be5bf-11ab3bc9fa9f9a740a00206a01a6673d-en-US>`_
                        
                        Arguments: IF, LO, LO1, LO2, RF
                        """
                        _cmd = "FIXed"
                        args = ["IF", "LO", "LO1", "LO2", "RF"]
                        
                    class FUNDamental(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:FUNDamental
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a1c4edf2d1ac45cf.htm#ID_8a511aeefa9fa9f50a00206a01692dac-c23eb715fa9fa33e0a00206a01a6673d-en-US>`_
                        
                        Arguments: IF, LO, LO1, LO2, RF
                        """
                        _cmd = "FUNDamental"
                        args = ["IF", "LO", "LO1", "LO2", "RF"]
                        
                    class IFFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:MIXer:IFFixed
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "IFFixed"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class IFPort(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:IFPort
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/61bcffd9773b4ef3.htm#ID_815f1cf4aaa81e3b0a00206a0081c154-9df8ed98aaa812730a00206a00dee6b8-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "IFPort"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class LOEXternal(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:MIXer:LOEXternal
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, NONE, SOURCE1, SOURCE2, UP
                        """
                        _cmd = "LOEXternal"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "NONE", "SOURCE1", "SOURCE2", "UP"]
                        
                    class LOFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:MIXer:LOFixed
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "LOFixed"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class LOINternal(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:MIXer:LOINternal
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, NONE, UP
                        """
                        _cmd = "LOINternal"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "NONE", "UP"]
                        
                    class LOMultiplier(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:LOMultiplier
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/743380a33eda455c.htm#ID_f3d77c26aaa82d3e0a00206a0170f2da-d163fc66aaa821860a00206a00dee6b8-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "LOMultiplier"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class LOPort(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:LOPort
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/74fe7d03764c4a7f.htm#ID_6a4729ceaaa83b090a00206a01c4bfbd-de91c582aaa8301d0a00206a00dee6b8-en-US>`_
                        
                        Arguments: GENerator, NONE, PORT
                        """
                        _cmd = "LOPort"
                        args = ["GENerator", "NONE", "PORT"]
                        
                    class MFFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:MFFixed
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6b15b2a135cf44f0.htm#ID_be2dd1ceaaa848480a00206a004f1b7e-328d8895aaa83d6b0a00206a00dee6b8-en-US>`_
                        
                        Arguments: IF, LO, LO1, LO2, RF
                        """
                        _cmd = "MFFixed"
                        args = ["IF", "LO", "LO1", "LO2", "RF"]
                        
                    class RFFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        SENSe:FREQuency:CONVersion:MIXer:RFFixed
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "RFFixed"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class RFMultiplier(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:RFMultiplier
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f8796452875f445f.htm#ID_d37d6ecbaaa856ee0a00206a01f7adfa-b1ce8fe7aaa84bd20a00206a00dee6b8-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "RFMultiplier"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class RFPort(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:RFPort
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e433724a23fd4a9e.htm#ID_9356f065aaa863900a00206a004b1cf6-82c43f97aaa859400a00206a00dee6b8-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "RFPort"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class STAGes(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:STAGes
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c8e19d7d125445db.htm#ID_1ef50da0aaa872460a00206a01ceb9d1-40349cbeaaa8665f0a00206a00dee6b8-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "STAGes"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class TFRequency(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:CONVersion:MIXer:TFRequency
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/52f5e8c3a19d41ca.htm#ID_51f82e6cfa9feac60a00206a002e1df4-7cc304a8fa9fe4000a00206a01a6673d-en-US>`_
                        
                        Arguments: BAND1, BAND2, DCLower, DCUPper, UCONversion
                        """
                        _cmd = "TFRequency"
                        args = ["BAND1", "BAND2", "DCLower", "DCUPper", "UCONversion"]
                        
            class CW(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:CW
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f9c9976fdd0f4f39.htm#ID_2ac09567faa0b2f80a00206a013090e9-fc5e7f70faa0ad4a0a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CW"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class FIXed(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:FIXed
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f9c9976fdd0f4f39.htm#ID_731505e2fa9ff2480a00206a01158020-7d13c8dafa9fec9b0a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "FIXed"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class IMODulation(SCPINode):
                """
                SENSe:FREQuency:IMODulation
                
                Arguments: 
                """
                _cmd = "IMODulation"
                args = [""]
                
                class CONVersion(SCPINode, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:CONVersion
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4d584eff06f84733.htm#ID_23fcb342faa0017b0a00206a00b25587-58d97526fa9ffbce0a00206a01a6673d-en-US>`_
                    
                    Arguments: OFF
                    """
                    _cmd = "CONVersion"
                    args = ["OFF"]
                    
                class LTONe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:LTONe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ab3534c8bace41b4.htm#ID_5bf57addfaa0091c0a00206a0142fa1e-01793a61faa0035f0a00206a01a6673d-en-US>`_
                    
                    Arguments: GENerator, NONE, PORT
                    """
                    _cmd = "LTONe"
                    args = ["GENerator", "NONE", "PORT"]
                    
                class ORDer(SCPINodeN, SCPIBool):
                    """
                    SENSe:FREQuency:IMODulation:ORDer
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "ORDer"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SENSe:FREQuency:IMODulation:ORDer:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8ad47d678f7f436b.htm#ID_06e1352dfaa010ad0a00206a003c0b60-aac10042faa00af00a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class RECeiver(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:RECeiver
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e1eb2d7b18c24a08.htm#ID_b274a1ddfaa0186e0a00206a0161499f-bf9aaa56faa012920a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "RECeiver"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class SPECtrum(SCPINode, SCPIBool):
                    """
                    SENSe:FREQuency:IMODulation:SPECtrum
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "SPECtrum"
                    args = ["1", "OFF", "ON"]
                    
                    class MORDer(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:FREQuency:IMODulation:SPECtrum:MORDer
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b0c80ebe3fe84751.htm#ID_4245b5cdfaa0207c0a00206a0107003e-ab9dd1fffaa01a520a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "MORDer"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SENSe:FREQuency:IMODulation:SPECtrum:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3bf0c8d352974b60.htm#ID_01be2623faa029850a00206a018c40e0-1e47673cfaa0229f0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class TDIStance(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:TDIStance
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a7c1836cab484001.htm#ID_aafb6b64faa032bc0a00206a011bedae-83b2e89cfaa02bc70a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "TDIStance"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class TTOutput(SCPINode, SCPIQuery, SCPISet):
                    """
                    SENSe:FREQuency:IMODulation:TTOutput
                    
                    Arguments: EDEVice, PORT
                    """
                    _cmd = "TTOutput"
                    args = ["EDEVice", "PORT"]
                    
                class UTONe(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:IMODulation:UTONe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ff61ec52404c4930.htm#ID_63f13342faa046530a00206a012e0ff3-67fe67dbfaa03f5e0a00206a01a6673d-en-US>`_
                    
                    Arguments: GENerator, NONE, PORT
                    """
                    _cmd = "UTONe"
                    args = ["GENerator", "NONE", "PORT"]
                    
            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:MODE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/208318e5658e49fa.htm#ID_fe506898faa08cd20a00206a01a4bc44-203297cdfaa086e60a00206a01a6673d-en-US>`_
                
                Arguments: CW, FIXed, SEGMent, SWEep
                """
                _cmd = "MODE"
                args = ["CW", "FIXed", "SEGMent", "SWEep"]
                
            class SBANd(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:SBANd
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/020d819cc9124330.htm#ID_18e53f5efaa094830a00206a0157f1ef-0a15cef1faa08eb60a00206a01a6673d-en-US>`_
                
                Arguments: AUTO, NEGative, POSitive
                """
                _cmd = "SBANd"
                args = ["AUTO", "NEGative", "POSitive"]
                
            class SEGMent(SCPINode):
                """
                SENSe:FREQuency:SEGMent
                
                Arguments: 
                """
                _cmd = "SEGMent"
                args = [""]
                
                class AXIS(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:FREQuency:SEGMent:AXIS
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/79ff3cfca02d43db.htm#ID_e107f4ce6129d6200a00206a002cf90e-16bf461d6129cde30a00206a01ed2866-en-US>`_
                    
                    Arguments: FREQuency, POINt
                    """
                    _cmd = "AXIS"
                    args = ["FREQuency", "POINt"]
                    
            class SPAN(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:SPAN
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/880fb7cf42594d10.htm#ID_19d721c4faa09c240a00206a01889fa1-5f6f4612faa096670a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "SPAN"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class STARt(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:STARt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/62a9e33d543548b1.htm#ID_cb181842faa0a3d50a00206a0130d1a9-3b77cf21faa09df90a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "STARt"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class STOP(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FREQuency:STOP
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/62a9e33d543548b1.htm#ID_8da94e0ffaa0ab560a00206a001393fe-a4f0d36bfaa0a5b90a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "STOP"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
        class FUNCtion(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:FUNCtion
            
            Arguments: 'string'
            """
            _cmd = "FUNCtion"
            args = ["'string'"]
            
            class ON(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:FUNCtion:ON
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a60c5184e5484818.htm#ID_5611a1c6faaa7b640a00206a00e83a51-a685455efaaa75a70a00206a01a6673d-en-US>`_
                
                Arguments: 'XFRequency:POWer:A1', 'XFRequency:POWer:B1', 'XFRequency:POWer:KFACtor', 'XFRequency:POWer:MUFactor1', 'XFRequency:POWer:RATio', 'XFRequency:POWer:S1', 'XFRequency:POWer:S1:DUMMy', 'XFRequency:POWer:Y1', 'XFRequency:POWer:Z1', 'XFRequency:VOLTage', 'XFRequency:VOLTage:DC', 'XPOWer:POWer:A1', 'XPOWer:POWer:B1', 'XPOWer:POWer:RATio', 'XPOWer:POWer:S1', 'XPOWer:POWer:S1:DUMMy', 'XPOWer:POWer:Y1', 'XPOWer:POWer:Z1', 'XPOWer:VOLTage', 'XPOWer:VOLTage:DC', 'XTIMe:POWer:A1', 'XTIMe:POWer:B1', 'XTIMe:POWer:KFACtor', 'XTIMe:POWer:MUFactor1', 'XTIMe:POWer:RATio', 'XTIMe:POWer:S1', 'XTIMe:POWer:S1:DUMMy', 'XTIMe:POWer:Y1', 'XTIMe:POWer:Z1', 'XTIMe:VOLTage', 'XTIMe:VOLTage:DC'
                """
                _cmd = "ON"
                args = ["'XFRequency:POWer:A1'", "'XFRequency:POWer:B1'", "'XFRequency:POWer:KFACtor'", "'XFRequency:POWer:MUFactor1'", "'XFRequency:POWer:RATio'", "'XFRequency:POWer:S1'", "'XFRequency:POWer:S1:DUMMy'", "'XFRequency:POWer:Y1'", "'XFRequency:POWer:Z1'", "'XFRequency:VOLTage'", "'XFRequency:VOLTage:DC'", "'XPOWer:POWer:A1'", "'XPOWer:POWer:B1'", "'XPOWer:POWer:RATio'", "'XPOWer:POWer:S1'", "'XPOWer:POWer:S1:DUMMy'", "'XPOWer:POWer:Y1'", "'XPOWer:POWer:Z1'", "'XPOWer:VOLTage'", "'XPOWer:VOLTage:DC'", "'XTIMe:POWer:A1'", "'XTIMe:POWer:B1'", "'XTIMe:POWer:KFACtor'", "'XTIMe:POWer:MUFactor1'", "'XTIMe:POWer:RATio'", "'XTIMe:POWer:S1'", "'XTIMe:POWer:S1:DUMMy'", "'XTIMe:POWer:Y1'", "'XTIMe:POWer:Z1'", "'XTIMe:VOLTage'", "'XTIMe:VOLTage:DC'"]
                
        class HARMonic(SCPINode):
            """
            SENSe:HARMonic
            
            Arguments: 
            """
            _cmd = "HARMonic"
            args = [""]
            
            class AUTO(SCPINode, SCPIBool):
                """
                `SENSe:HARMonic:AUTO
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f961e1983ade4927.htm#ID_bb76c36488f5366e0a001ae7426087b1-ea24a49588f535450a001ae77b2dc49c-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "AUTO"
                args = ["1", "OFF", "ON"]
                
            class DLENgth(SCPINode):
                """
                SENSe:HARMonic:DLENgth
                
                Arguments: 
                """
                _cmd = "DLENgth"
                args = [""]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:HARMonic:DLENgth:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4f31b3da63404c9d.htm#ID_8a861e5688f538330a001ae732d6903c-cd7a4f3388f537290a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class RTIMe(SCPINode):
                """
                SENSe:HARMonic:RTIMe
                
                Arguments: 
                """
                _cmd = "RTIMe"
                args = [""]
                
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:HARMonic:RTIMe:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a337292cdf284f75.htm#ID_a836bc7788f539f80a001ae747e30563-5bbfc21088f5390e0a001ae77b2dc49c-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DATA"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class THReshold(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:HARMonic:RTIMe:THReshold
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ada5d90702ab4b38.htm#ID_d5c7c7c288f53b7f0a001ae77b69f9aa-2113501a88f53a940a001ae77b2dc49c-en-US>`_
                    
                    Arguments: T1_9, T2_8
                    """
                    _cmd = "THReshold"
                    args = ["T1_9", "T2_8"]
                    
        class LPORt(SCPINodeN):
            """
            SENSe:LPORt
            
            Arguments: 
            """
            _cmd = "LPORt"
            args = [""]
            
            class ZCOMmon(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:LPORt:ZCOMmon
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ff5f3222ee424c70.htm#ID_94158978faa1977b0a00206a00b62876-b7b2e2a9faa191ce0a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "ZCOMmon"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class ZDEFault(SCPINode, SCPIBool):
                """
                SENSe:LPORt:ZDEFault
                
                Arguments: 1, OFF, ON
                """
                _cmd = "ZDEFault"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `SENSe:LPORt:ZDEFault:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b5192de6d67e4e20.htm#ID_b2a7efd9a6eae2890a001ae748b54b6c-29d33fd7a6eae0f30a001ae729ca0bb3-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class ZDIFferent(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:LPORt:ZDIFferent
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ff5f3222ee424c70.htm#ID_96565f11faa19f0c0a00206a00efad8e-ed441534faa199500a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "ZDIFferent"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
        class PAE(SCPINode):
            """
            SENSe:PAE
            
            Arguments: 
            """
            _cmd = "PAE"
            args = [""]
            
            class DCINput(SCPINode):
                """
                SENSe:PAE:DCINput
                
                Arguments: 
                """
                _cmd = "DCINput"
                args = [""]
                
                class MAIN(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PAE:DCINput:MAIN
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6fc282982d944daf.htm#ID_356ca9e6612ad1960a00206a008832d6-0a4f4b44612ac12b0a00206a01ed2866-en-US>`_
                    
                    Arguments: DC1, DC2, DC3, DC4
                    """
                    _cmd = "MAIN"
                    args = ["DC1", "DC2", "DC3", "DC4"]
                    
                class SECondary(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PAE:DCINput:SECondary
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bcee4f6f0bb44595.htm#ID_53a5ef24612ae56c0a00206a01de3061-47c198ac612ad7530a00206a01ed2866-en-US>`_
                    
                    Arguments: DC1, DC2, DC3, DC4
                    """
                    _cmd = "SECondary"
                    args = ["DC1", "DC2", "DC3", "DC4"]
                    
            class PARameters(SCPINode):
                """
                SENSe:PAE:PARameters
                
                Arguments: 
                """
                _cmd = "PARameters"
                args = [""]
                
                class I(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PAE:PARameters:I
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/77a78fdc8983460b.htm#ID_70ab057e612a25690a00206a0159a980-61443cbe612a1e830a00206a01ed2866-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "I"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class R(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PAE:PARameters:R
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b8cc1a404aae4a06.htm#ID_cdd9f751612a2f8b0a00206a007085fc-71778e41612a28090a00206a01ed2866-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "R"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class U(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:PAE:PARameters:U
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1412c2ce185c4b54.htm#ID_47333546612a392f0a00206a0172f758-80c4866f612a31dc0a00206a01ed2866-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "U"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class TYPE(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:PAE:TYPE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5425e7f0f7b24f8a.htm#ID_da0fd500612afa6b0a00206a006111f7-dab87b46612aed8a0a00206a01ed2866-en-US>`_
                
                Arguments: CURRent, VCURrent, VOLTage
                """
                _cmd = "TYPE"
                args = ["CURRent", "VCURrent", "VOLTage"]
                
        class PORT(SCPINodeN):
            """
            SENSe:PORT
            
            Arguments: 
            """
            _cmd = "PORT"
            args = [""]
            
            class ZREFerence(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:PORT:ZREFerence
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9e4c4942dcf04a10.htm#ID_307cb740faa1b7b50a00206a0149fb85-20b51d47faa1b2080a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "ZREFerence"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
        class POWer(SCPINode):
            """
            SENSe:POWer
            
            Arguments: 
            """
            _cmd = "POWer"
            args = [""]
            
            class AGCMode(SCPINodeN):
                """
                SENSe:POWer:AGCMode
                
                Arguments: 
                """
                _cmd = "AGCMode"
                args = [""]
                
                class ACQuire(SCPINode, SCPISet):
                    """
                    `SENSe:POWer:AGCMode:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f6d3c2eb53224cd3.htm#ID_287e0e5b5de650020a002019005cd65d-61ceda195de64ec90a0020190152315a-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "ACQuire"
                    args = [""]
                    
                class MEASure(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:POWer:AGCMode:MEASure
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/02847cb715004998.htm#ID_818b778e135527390a00206a0179ba91-f9b489121355216d0a00206a0182dc26-en-US>`_
                    
                    Arguments: AUTO, LDIStortion, LNOise
                    """
                    _cmd = "MEASure"
                    args = ["AUTO", "LDIStortion", "LNOise"]
                    
                class SAVE(SCPINode, SCPISet):
                    """
                    `SENSe:POWer:AGCMode:SAVE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a69c75b84ab946d7.htm#ID_467705d35de651e60a002019015c7244-7af5781c5de650bd0a0020190152315a-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "SAVE"
                    args = [""]
                    
            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:POWer:ATTenuation
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/04a79a1d70d0496d.htm#ID_187ea6a6faa1bf460a00206a008dacb9-7302ebeefaa1b9990a00206a01a6673d-en-US>`_
                
                Arguments: 1, ARECeiver, BRECeiver, CRECeiver, DEFault, DOWN, DRECeiver, MAXimum, MINimum, UP
                """
                _cmd = "ATTenuation"
                args = ["1", "ARECeiver", "BRECeiver", "CRECeiver", "DEFault", "DOWN", "DRECeiver", "MAXimum", "MINimum", "UP"]
                
            class GAINcontrol(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:POWer:GAINcontrol
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/02bdb8f60bae4be0.htm#ID_b94cb83baaa880010a00206a0033f802-17c67bf9aaa875340a00206a00dee6b8-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "GAINcontrol"
                args = ["'string'"]
                
                class GLOBal(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:POWer:GAINcontrol:GLOBal
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6a22d5d655e84479.htm#ID_4c6eef1eaaa88fa10a00206a003fbf40-763d4d64aaa8838b0a00206a00dee6b8-en-US>`_
                    
                    Arguments: AUTO, LDIStortion, LNOise, MANual
                    """
                    _cmd = "GLOBal"
                    args = ["AUTO", "LDIStortion", "LNOise", "MANual"]
                    
            class IFGain(SCPINodeN):
                """
                SENSe:POWer:IFGain
                
                Arguments: 
                """
                _cmd = "IFGain"
                args = [""]
                
                class MEASure(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:POWer:IFGain:MEASure
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/02847cb715004998.htm#ID_b103b97afaa1c7350a00206a01f123cc-0f4f1ee9faa1c13a0a00206a01a6673d-en-US>`_
                    
                    Arguments: AUTO, LDIStortion, LNOise
                    """
                    _cmd = "MEASure"
                    args = ["AUTO", "LDIStortion", "LNOise"]
                    
        class ROSCillator(SCPINode, SCPIQuery, SCPISet):
            """
            SENSe:ROSCillator
            
            Arguments: EXTernal, INTernal
            """
            _cmd = "ROSCillator"
            args = ["EXTernal", "INTernal"]
            
            class EXTernal(SCPINode):
                """
                SENSe:ROSCillator:EXTernal
                
                Arguments: 
                """
                _cmd = "EXTernal"
                args = [""]
                
                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:ROSCillator:EXTernal:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8fdadbfdb9f9447f.htm#ID_6c4e79f3faa938c30a00206a013d1159-f5402c6afaa933070a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "FREQuency"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:ROSCillator:SOURce
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4314a7accd124cd8.htm#ID_c2c6217dfaa940550a00206a018060f9-42609acffaa93aa80a00206a01a6673d-en-US>`_
                
                Arguments: EXTernal, INTernal
                """
                _cmd = "SOURce"
                args = ["EXTernal", "INTernal"]
                
        class SEGMent(SCPINodeN, SCPIBool):
            """
            SENSe:SEGMent
            
            Arguments: 1, OFF, ON
            """
            _cmd = "SEGMent"
            args = ["1", "OFF", "ON"]
            
            class ADD(SCPINode, SCPISet):
                """
                `SENSe:SEGMent:ADD
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8b499c72016147ec.htm#ID_42e94b09faa947f60a00206a01e7a868-404ea7abfaa942390a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "ADD"
                args = [""]
                
            class BWIDth(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SEGMent:BWIDth
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "BWIDth"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class RESolution(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:BWIDth:RESolution
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7f78d4cc550a43b4.htm#ID_a5fd34d6faa94f870a00206a0178a961-ff41de80faa949cb0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "RESolution"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                    class CONTrol(SCPINode, SCPIBool):
                        """
                        `SENSe:SEGMent:BWIDth:RESolution:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/85e00dbdac574895.htm#ID_7c9ad63afaa957280a00206a007d7923-baaeef63faa9516c0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "CONTrol"
                        args = ["1", "OFF", "ON"]
                        
                    class SELect(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SENSe:SEGMent:BWIDth:RESolution:SELect
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8ea6af2b51f94fd7.htm#ID_1347f01dfaa95f080a00206a01678d97-70ffbea1faa9590d0a00206a01a6673d-en-US>`_
                        
                        Arguments: HIGH, MEDium, NORMal
                        """
                        _cmd = "SELect"
                        args = ["HIGH", "MEDium", "NORMal"]
                        
                        class CONTrol(SCPINode, SCPIBool):
                            """
                            `SENSe:SEGMent:BWIDth:RESolution:SELect:CONTrol
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d4fd2f19549e4c8c.htm#ID_77b69576faa966d80a00206a012e13eb-1431397ffaa960ec0a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "CONTrol"
                            args = ["1", "OFF", "ON"]
                            
            class CLEar(SCPINode, SCPISet):
                """
                `SENSe:SEGMent:CLEar
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1e338ccd879849cc.htm#ID_ae21c7cdfaa96ec70a00206a00399727-eec3d465faa968eb0a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "CLEar"
                args = [""]
                
            class COUNt(SCPINode, SCPIQuery):
                """
                `SENSe:SEGMent:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cc92badd888e4893.htm#ID_0aedf98efaa976b60a00206a015e9478-74d2e61cfaa970da0a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "COUNt"
                args = [""]
                
            class DEFine(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:DEFine
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0fdd5bb7773c4237.htm#ID_68fd9307faa97e670a00206a007b59ed-faf43db76d4c9ff90a00206a00d96734-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "DEFine"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:DEFine:SELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5d2d463b271f465e.htm#ID_104e6acbfaa985f90a00206a013334f3-d97a540afaa9804c0a00206a01a6673d-en-US>`_
                    
                    Arguments: DWELl, SWTime
                    """
                    _cmd = "SELect"
                    args = ["DWELl", "SWTime"]
                    
            class DELete(SCPINodeN, SCPIQuery, SCPISet):
                """
                SENSe:SEGMent:DELete
                
                Arguments: 
                """
                _cmd = "DELete"
                args = [""]
                
                class ALL(SCPINode, SCPISet):
                    """
                    `SENSe:SEGMent:DELete:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ab5e9487d6324d5d.htm#ID_d97d6288faa98db90a00206a0151f78f-1bf10634faa987ed0a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "ALL"
                    args = [""]
                    
                class DUMMy(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:DELete:DUMMy
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8b87412b453542e4.htm#ID_e3d18ac5faa9955a0a00206a009f336d-55db9b98faa98f9d0a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "DUMMy"
                    args = [""]
                    
            class FREQuency(SCPINode):
                """
                SENSe:SEGMent:FREQuency
                
                Arguments: 
                """
                _cmd = "FREQuency"
                args = [""]
                
                class CENTer(SCPINode, SCPIQuery):
                    """
                    `SENSe:SEGMent:FREQuency:CENTer
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b20419a51aad471f.htm#ID_94785a74faa99cdc0a00206a01d13180-4e26a2dcfaa9974e0a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "CENTer"
                    args = [""]
                    
                class SPAN(SCPINode, SCPIQuery):
                    """
                    `SENSe:SEGMent:FREQuency:SPAN
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b20419a51aad471f.htm#ID_00b1210dfaa9a46d0a00206a00bfcdb7-5367f9bffaa99ed00a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "SPAN"
                    args = [""]
                    
                class STARt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:FREQuency:STARt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e6eca9c9cd1b422a.htm#ID_642356f7faa9abff0a00206a010d9e37-ddfabe24faa9a6520a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "STARt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class STOP(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:FREQuency:STOP
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e6eca9c9cd1b422a.htm#ID_e9561eb0faa9b3710a00206a002ba8aa-3587e257faa9add40a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "STOP"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class INSert(SCPINodeN, SCPIQuery, SCPISet):
                """
                `SENSe:SEGMent:INSert
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a43fbabbfb8548ed.htm#ID_edfe071ffaa9bb510a00206a00232fd5-402184618754dbd40a00206a00048ead-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "INSert"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class SELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:INSert:SELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/53faae429fbd4847.htm#ID_b802bcedfaa9c2f20a00206a00e943e9-dfd68ad3faa9bd640a00206a01a6673d-en-US>`_
                    
                    Arguments: DWELl, SWTime
                    """
                    _cmd = "SELect"
                    args = ["DWELl", "SWTime"]
                    
            class OVERlap(SCPINode, SCPIBool):
                """
                `SENSe:SEGMent:OVERlap
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d07bb6d0c6004991.htm#ID_ce5c83b4faa9cac20a00206a01aa0f97-808993ecfaa9c4d60a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "OVERlap"
                args = ["1", "OFF", "ON"]
                
            class POWer(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SEGMent:POWer
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "POWer"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class GAINcontrol(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:POWer:GAINcontrol
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3efd8069d3aa445a.htm#ID_506a9a45aaa8a0a80a00206a014de620-c49903a0aaa892ed0a00206a00dee6b8-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "GAINcontrol"
                    args = ["'string'"]
                    
                    class CONTrol(SCPINode, SCPIBool):
                        """
                        `SENSe:SEGMent:POWer:GAINcontrol:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9608e4d687cd4b33.htm#ID_55e47952aaa8ae450a00206a01d7002f-41fdea03aaa8a3770a00206a00dee6b8-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "CONTrol"
                        args = ["1", "OFF", "ON"]
                        
                class LEVel(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:POWer:LEVel
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/41f669a6f1ca47df.htm#ID_c32c7991faa9d2b10a00206a01709402-1a1b2272faa9cc970a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "LEVel"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                    class CONTrol(SCPINode, SCPIBool):
                        """
                        `SENSe:SEGMent:POWer:LEVel:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bd27175de2174b8a.htm#ID_0889af7afaa9da230a00206a01faf0df-69290e76faa9d4950a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "CONTrol"
                        args = ["1", "OFF", "ON"]
                        
            class STATe(SCPINode, SCPIBool):
                """
                `SENSe:SEGMent:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d3960bdbcfeb49f4.htm#ID_6dc91a91faaa0f4c0a00206a01341c39-ceac6573faaa09900a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
            class SWEep(SCPINode):
                """
                SENSe:SEGMent:SWEep
                
                Arguments: 
                """
                _cmd = "SWEep"
                args = [""]
                
                class DWELl(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:SWEep:DWELl
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ce5c1223ab0542ed.htm#ID_011fb27efaa9e1c40a00206a009027ec-1580ec0bfaa9dc170a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DWELl"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                    class CONTrol(SCPINode, SCPIBool):
                        """
                        `SENSe:SEGMent:SWEep:DWELl:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dabe778ff0364c84.htm#ID_8056275efaa9e9750a00206a003922be-67d1b540faa9e3a90a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "CONTrol"
                        args = ["1", "OFF", "ON"]
                        
                class GENeration(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:SWEep:GENeration
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6ac02dfba9164182.htm#ID_7dff9430cf938f4d0a001ae76592e970-55859ec9cf938da70a001ae7061b2cf6-en-US>`_
                    
                    Arguments: ANALog, STEPped
                    """
                    _cmd = "GENeration"
                    args = ["ANALog", "STEPped"]
                    
                class POINts(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:SWEep:POINts
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/52d5a10625e64a82.htm#ID_04a142bffaa9f0e70a00206a01076885-20e0b786faa9eb4a0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "POINts"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SEGMent:SWEep:TIME
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/37b7c642120149da.htm#ID_f5b6df0ffaa9f8a80a00206a013a9a75-542f6badfaa9f2fb0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "TIME"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                    class CONTrol(SCPINode, SCPIBool):
                        """
                        `SENSe:SEGMent:SWEep:TIME:CONTrol
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ff129a9296e54210.htm#ID_a22e28fffaaa00390a00206a0084a14b-e9c5fc67faa9fa8c0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "CONTrol"
                        args = ["1", "OFF", "ON"]
                        
                    class SUM(SCPINode, SCPIQuery):
                        """
                        `SENSe:SEGMent:SWEep:TIME:SUM
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/89fbe395bfe44bc6.htm#ID_b1ba9049faaa07bb0a00206a0168c693-2fa53146faaa020e0a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "SUM"
                        args = [""]
                        
        class SWEep(SCPINode):
            """
            SENSe:SWEep
            
            Arguments: 
            """
            _cmd = "SWEep"
            args = [""]
            
            class AXIS(SCPINode):
                """
                SENSe:SWEep:AXIS
                
                Arguments: 
                """
                _cmd = "AXIS"
                args = [""]
                
                class FREQuency(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:AXIS:FREQuency
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8416b68505d74b1f.htm#ID_5571db31faaa18360a00206a01d696e2-91a48f48faaa12690a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "FREQuency"
                    args = ["'string'"]
                    
                class POWer(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:AXIS:POWer
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cfd456caf566495d.htm#ID_a33dcc53faaa1fb80a00206a016ce603-ccb15a96faaa1a2a0a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "POWer"
                    args = ["'string'"]
                    
            class COUNt(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5cb1268b17f34710.htm#ID_16e99ab0faaa27490a00206a008e95d3-fd50d4b6faaa21ac0a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "COUNt"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class ALL(SCPINode, SCPISet):
                    """
                    `SENSe:SWEep:COUNt:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e111584.htm#ID_b22fd8a02b98b6df0a00206a00b47198-7af948622b98af1e0a00206a0020d3a0-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "ALL"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class DETector(SCPINode):
                """
                SENSe:SWEep:DETector
                
                Arguments: 
                """
                _cmd = "DETector"
                args = [""]
                
                class TIME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:DETector:TIME
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5e638bbfd9ca4218.htm#ID_6bf27c90faaa2efa0a00206a00bbbd04-fe2114b5faaa294d0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "TIME"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class DWELl(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:DWELl
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/48bb45e33ab64490.htm#ID_c04c664efaaa36ca0a00206a01e7ac36-1d281f10faaa30de0a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "DWELl"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class IPOint(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SENSe:SWEep:DWELl:IPOint
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8e067eefd1e34640.htm#ID_030aed4fbba8fcb80a00201901c6f0bf-a6d51bb2bba8fb7f0a0020190170f726-en-US>`_
                    
                    Arguments: ALL, FIRSt
                    """
                    _cmd = "IPOint"
                    args = ["ALL", "FIRSt"]
                    
            class GENeration(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:GENeration
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2298b3dd1e844065.htm#ID_7ee8413cfaaa3e5b0a00206a00e2e4dc-8f0aff4cfaaa389e0a00206a01a6673d-en-US>`_
                
                Arguments: ANALog, STEPped
                """
                _cmd = "GENeration"
                args = ["ANALog", "STEPped"]
                
                class ANALog(SCPINode):
                    """
                    SENSe:SWEep:GENeration:ANALog
                    
                    Arguments: 
                    """
                    _cmd = "ANALog"
                    args = [""]
                    
                    class CONDition(SCPINode, SCPIQuery):
                        """
                        `SENSe:SWEep:GENeration:ANALog:CONDition
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c804742dafba418c.htm#ID_4422091acf9397d90a001ae74b49912d-26ef356bcf9395580a001ae7061b2cf6-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "CONDition"
                        args = [""]
                        
            class MODE(SCPINode, SCPIQuery, SCPISet):
                """
                SENSe:SWEep:MODE
                
                Arguments: CONTinuous, HOLD
                """
                _cmd = "MODE"
                args = ["CONTinuous", "HOLD"]
                
            class POINts(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:POINts
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/68b77d9828354b78.htm#ID_eaf7e123faaa4d8e0a00206a00265a51-df944ab9faaa47d10a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "POINts"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class SPACing(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:SPACing
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f3498d3b009e4326.htm#ID_fcf6483afaaa553e0a00206a0166926c-c3423ddbfaaa4f820a00206a01a6673d-en-US>`_
                
                Arguments: LINear, LOGarithmic
                """
                _cmd = "SPACing"
                args = ["LINear", "LOGarithmic"]
                
            class SRCPort(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:SRCPort
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/31cb07b38fbe4454.htm#ID_06884359faaa9a270a00206a01493bc8-eb083f47faaa944b0a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "SRCPort"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class STEP(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:STEP
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6958d4fb3c5642a2.htm#ID_34eced8ffaaa5cef0a00206a0034523e-8bc6b624faaa57520a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "STEP"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class TIME(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:TIME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8227ae4383e449fe.htm#ID_68a69f3cfaaa64810a00206a010d0e5b-25292a32faaa5ee30a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "TIME"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class AUTO(SCPINode, SCPIBool):
                    """
                    `SENSe:SWEep:TIME:AUTO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4e1073e7fde645a8.htm#ID_7134b8a5faaa6c310a00206a002ca1b5-cd3732cffaaa66650a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "AUTO"
                    args = ["1", "OFF", "ON"]
                    
            class TYPE(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:SWEep:TYPE
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/3092cc2858af4096.htm#ID_b8dccd81faaa73d30a00206a018614c7-c134571ffaaa6e060a00206a01a6673d-en-US>`_
                
                Arguments: CW, LINear, LOGarithmic, POINt, POWer, SEGMent
                """
                _cmd = "TYPE"
                args = ["CW", "LINear", "LOGarithmic", "POINt", "POWer", "SEGMent"]
                
        class UDSParams(SCPINodeN):
            """
            SENSe:UDSParams
            
            Arguments: 
            """
            _cmd = "UDSParams"
            args = [""]
            
            class ACTive(SCPINode, SCPIBool):
                """
                `SENSe:UDSParams:ACTive
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6648d86a94534c05.htm#ID_98fbfd15842ed63e0a002019008f7696-77db25eb842ed4c70a00201901936165-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "ACTive"
                args = ["1", "OFF", "ON"]
                
            class PARam(SCPINode, SCPIQuery, SCPISet):
                """
                `SENSe:UDSParams:PARam
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9862134a154b4fea.htm#ID_6e316dbd842ed8610a002019005592c6-0069e2d3842ed6db0a00201901936165-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "PARam"
                args = ["'string'"]
                
    class SOURce(SCPINodeN):
        """
        SOURce
        
        Arguments: 
        """
        _cmd = "SOURce"
        args = [""]
        
        class FREQuency(SCPINodeN, SCPIQuery, SCPISet):
            """
            SOURce:FREQuency
            
            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "FREQuency"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
            
            class CONVersion(SCPINode):
                """
                SOURce:FREQuency:CONVersion
                
                Arguments: 
                """
                _cmd = "CONVersion"
                args = [""]
                
                class ARBitrary(SCPINode):
                    """
                    SOURce:FREQuency:CONVersion:ARBitrary
                    
                    Arguments: 
                    """
                    _cmd = "ARBitrary"
                    args = [""]
                    
                    class EFRequency(SCPINodeN, SCPIBool):
                        """
                        `SOURce:FREQuency:CONVersion:ARBitrary:EFRequency
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/323c75e925bb4524.htm#ID_b7a0eff3faaad3090a00206a0048d9a3-8f628099faaaccb00a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "EFRequency"
                        args = ["1", "OFF", "ON"]
                        
                    class IFRequency(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:ARBitrary:IFRequency
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/59b39faac9d34290.htm#ID_f158a498faaadb850a00206a016d54a1-dca8927efaaad52c0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "IFRequency"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class MIXer(SCPINode):
                    """
                    SOURce:FREQuency:CONVersion:MIXer
                    
                    Arguments: 
                    """
                    _cmd = "MIXer"
                    args = [""]
                    
                    class FUNDamental(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:CONVersion:MIXer:FUNDamental
                        
                        Arguments: LO, RF
                        """
                        _cmd = "FUNDamental"
                        args = ["LO", "RF"]
                        
                    class PFIXed(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:FREQuency:CONVersion:MIXer:PFIXed
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "PFIXed"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class PMFixed(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:MIXer:PMFixed
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/90e5b7d03ba1419a.htm#ID_dcd270fcaaa8bb350a00206a006b2206-a481c9f8aaa8b0870a00206a00dee6b8-en-US>`_
                        
                        Arguments: IF, LO, LO1, LO2, RF
                        """
                        _cmd = "PMFixed"
                        args = ["IF", "LO", "LO1", "LO2", "RF"]
                        
                    class PMODe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:FREQuency:CONVersion:MIXer:PMODe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6abc6f3ee12a4a89.htm#ID_eca305c5aaa8c8740a00206a010fb1c0-7aa0a2dfaaa8be420a00206a00dee6b8-en-US>`_
                        
                        Arguments: IF, LO, LO1, LO2, RF
                        """
                        _cmd = "PMODe"
                        args = ["IF", "LO", "LO1", "LO2", "RF"]
                        
            class CW(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:FREQuency:CW
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/53b73ef8963647ff.htm#ID_6590a713faaafaa60a00206a01616355-b65bc797faaaf4f90a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "CW"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class FIXed(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:FREQuency:FIXed
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/53b73ef8963647ff.htm#ID_a7452765faaaf3240a00206a011db4aa-5fe941c7faaaed670a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "FIXed"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
        class GROup(SCPINodeN, SCPIQuery, SCPISet):
            """
            `SOURce:GROup
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/fc145e54206141d3.htm#ID_57d9bdd7faab02280a00206a004a8d5f-d5e97631faaafc8a0a00206a01a6673d-en-US>`_
            
            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "GROup"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
            
            class CLEar(SCPINode, SCPISet):
                """
                `SOURce:GROup:CLEar
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/12c2fec8bb4c4781.htm#ID_ef09d686faab099a0a00206a01cdc798-26f736eafaab03fc0a00206a01a6673d-en-US>`_
                
                Arguments: ALL
                """
                _cmd = "CLEar"
                args = ["ALL"]
                
            class COUNt(SCPINode, SCPIQuery):
                """
                `SOURce:GROup:COUNt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/08e95afdda7f45ce.htm#ID_fdf34ed4faab110c0a00206a00d13624-44e4ccb9faab0b6f0a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "COUNt"
                args = [""]
                
            class DPORt(SCPINode):
                """
                SOURce:GROup:DPORt
                
                Arguments: 
                """
                _cmd = "DPORt"
                args = [""]
                
                class COUNt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:GROup:DPORt:COUNt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f23e4eb88b3d40cb.htm#ID_d643aadd4f3002f00a001ae721324d54-2c3bec494f30011b0a001ae7211c9327-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "COUNt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class NAME(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:GROup:NAME
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dc3c54b22c6c4d29.htm#ID_46aebfb54f3005320a001ae7202c9a7a-48b729ec4f3003bb0a001ae7211c9327-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "NAME"
                args = ["'string'"]
                
            class PORDer(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:GROup:PORDer
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8bb14661984542c4.htm#ID_4350a1c542b09baa0a001ae76aa5c44f-d807389542b09a420a001ae769a5b4da-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "PORDer"
                args = ["'string'"]
                
            class PORTs(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:GROup:PORTs
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0ce89bb991c34110.htm#ID_7894c65cfaab18ad0a00206a0114eedb-ffa24f1afaab12f00a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "PORTs"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class PPORt(SCPINodeN):
                """
                SOURce:GROup:PPORt
                
                Arguments: 
                """
                _cmd = "PPORt"
                args = [""]
                
                class DPORt(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:GROup:PPORt:DPORt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ca2c99de38a3435c.htm#ID_f929baf84f3008010a001ae7392085da-ccb6ff8f4f30065b0a001ae7211c9327-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DPORt"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
            class PPORts(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:GROup:PPORts
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/64383fd17c2f4ab3.htm#ID_103793c84f300aef0a001ae70a6fae59-1dd2cbc84f93c6540a001ae7068aeca9-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "PPORts"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class SIMultaneous(SCPINode):
                """
                SOURce:GROup:SIMultaneous
                
                Arguments: 
                """
                _cmd = "SIMultaneous"
                args = [""]
                
                class FOFFset(SCPINode):
                    """
                    SOURce:GROup:SIMultaneous:FOFFset
                    
                    Arguments: 
                    """
                    _cmd = "FOFFset"
                    args = [""]
                    
                    class CONDition(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:GROup:SIMultaneous:FOFFset:CONDition
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1b6cecbf09ac48a2.htm#ID_6677f2c5f72899280a001ae7416d538d-ddecae76f72897730a001ae743c5d16b-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "CONDition"
                        args = [""]
                        
                    class MOFFset(SCPINode):
                        """
                        SOURce:GROup:SIMultaneous:FOFFset:MOFFset
                        
                        Arguments: 
                        """
                        _cmd = "MOFFset"
                        args = [""]
                        
                        class BWFactor(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:GROup:SIMultaneous:FOFFset:MOFFset:BWFactor
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ce7864aa9d144bfd.htm#ID_5d682b89f7289c160a001ae74facad20-13412b41f7289a130a001ae743c5d16b-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "BWFactor"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class DVALue(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:GROup:SIMultaneous:FOFFset:MOFFset:DVALue
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c51184c526f44c54.htm#ID_90c896a2f7289ec60a001ae70134d207-eeacc11bf7289cd20a001ae743c5d16b-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "DVALue"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class MODE(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:GROup:SIMultaneous:FOFFset:MOFFset:MODE
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2645ca2926bf4b9d.htm#ID_e1280075f728a29e0a001ae70b3b58c9-ddf54056f7289ffe0a001ae743c5d16b-en-US>`_
                            
                            Arguments: BANDwidth, DIRect
                            """
                            _cmd = "MODE"
                            args = ["BANDwidth", "DIRect"]
                            
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:GROup:SIMultaneous:FOFFset:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2878dd518aae4b66.htm#ID_8e29ec05f728a6a50a001ae76efa6673-4d24d4f7f728a3e60a001ae743c5d16b-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
        class LPORt(SCPINodeN, SCPIQuery, SCPISet):
            """
            `SOURce:LPORt
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/49f764b18ad748ff.htm#ID_45afb15efaab202f0a00206a00ad1683-d5ab93aafaab1a910a00206a01a6673d-en-US>`_
            
            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "LPORt"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
            
            class CLEar(SCPINode, SCPISet):
                """
                `SOURce:LPORt:CLEar
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e2064f162cff4458.htm#ID_f7c17f6bfaab27a10a00206a00d8e015-8f1450e1faab22040a00206a01a6673d-en-US>`_
                
                Arguments: ALL
                """
                _cmd = "CLEar"
                args = ["ALL"]
                
        class POWer(SCPINodeN, SCPIQuery, SCPISet):
            """
            SOURce:POWer
            
            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "POWer"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
            
            class ALC(SCPINode):
                """
                SOURce:POWer:ALC
                
                Arguments: 
                """
                _cmd = "ALC"
                args = [""]
                
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:MODE
                    
                    Arguments: AUTO, BBANd, OFF, SBANd
                    """
                    _cmd = "MODE"
                    args = ["AUTO", "BBANd", "OFF", "SBANd"]
                    
                class SVARiable(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:ALC:SVARiable
                    
                    Arguments: AWAVe, BWAVe, SFK
                    """
                    _cmd = "SVARiable"
                    args = ["AWAVe", "BWAVe", "SFK"]
                    
            class ATTenuation(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:ATTenuation
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "ATTenuation"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class AUTO(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:ATTenuation:AUTO
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "AUTO"
                    args = ["1", "OFF", "ON"]
                    
            class CORRection(SCPINode, SCPISet):
                """
                SOURce:POWer:CORRection
                
                Arguments: A1, A2, A3, A4, CONVerter, ESRC1, ESRC2, GENerator, PORT
                """
                _cmd = "CORRection"
                args = ["A1", "A2", "A3", "A4", "CONVerter", "ESRC1", "ESRC2", "GENerator", "PORT"]
                
                class ACQuire(SCPINode, SCPISet):
                    """
                    `SOURce:POWer:CORRection:ACQuire
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d611f3410d13473b.htm#ID_5975972bfaae5f3a0a00206a00433247-c9b39da2faae596e0a00206a01a6673d-en-US>`_
                    
                    Arguments: A1, A2, A3, A4, CONVerter, ESRC1, ESRC2, GENerator, PORT
                    """
                    _cmd = "ACQuire"
                    args = ["A1", "A2", "A3", "A4", "CONVerter", "ESRC1", "ESRC2", "GENerator", "PORT"]
                    
                    class VERification(SCPINode):
                        """
                        SOURce:POWer:CORRection:ACQuire:VERification
                        
                        Arguments: 
                        """
                        _cmd = "VERification"
                        args = [""]
                        
                        class RESult(SCPINode, SCPIQuery):
                            """
                            `SOURce:POWer:CORRection:ACQuire:VERification:RESult
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0467fd8923a74a33.htm#ID_10e7870afaae66ac0a00206a002942b3-138b97a9faae611f0a00206a01a6673d-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "RESult"
                            args = [""]
                            
                class COLLect(SCPINode, SCPISet):
                    """
                    SOURce:POWer:CORRection:COLLect
                    
                    Arguments: ASENsor, BSENsor
                    """
                    _cmd = "COLLect"
                    args = ["ASENsor", "BSENsor"]
                    
                    class ACQuire(SCPINode, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:ACQuire
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/62891a00782d4b17.htm#ID_e8b93b83faadd71f0a00206a01d443f7-be19ecfffaadd1910a00206a01a6673d-en-US>`_
                        
                        Arguments: ASENsor, BSENsor
                        """
                        _cmd = "ACQuire"
                        args = ["ASENsor", "BSENsor"]
                        
                        class VERification(SCPINode, SCPIBool):
                            """
                            SOURce:POWer:CORRection:COLLect:ACQuire:VERification
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "VERification"
                            args = ["1", "OFF", "ON"]
                            
                            class STATe(SCPINode, SCPIBool):
                                """
                                SOURce:POWer:CORRection:COLLect:ACQuire:VERification:STATe
                                
                                Arguments: 1, OFF, ON
                                """
                                _cmd = "STATe"
                                args = ["1", "OFF", "ON"]
                                
                    class AVERage(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:CORRection:COLLect:AVERage
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "AVERage"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                        class COUNt(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:COLLect:AVERage:COUNt
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f67677c7002d4509.htm#ID_bf5b43d3faadaa520a00206a01a628d2-72b9973ffaada4b50a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "COUNt"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class NTOLerance(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:COLLect:AVERage:NTOLerance
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/84fccbafdbda4d27.htm#ID_d92c259efaada2e00a00206a00f34412-cabca395faad9d430a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "NTOLerance"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                    class CFACtor(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:CFACtor
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bd429ac245854fce.htm#ID_68824478faadb1d40a00206a00475d07-e8b2b329faadac370a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "CFACtor"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class FLATness(SCPINode, SCPIBool):
                        """
                        SOURce:POWer:CORRection:COLLect:FLATness
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "FLATness"
                        args = ["1", "OFF", "ON"]
                        
                    class METHod(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:CORRection:COLLect:METHod
                        
                        Arguments: PMONly, RRAFter, RRONly
                        """
                        _cmd = "METHod"
                        args = ["PMONly", "RRAFter", "RRONly"]
                        
                    class PMReadings(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:COLLect:PMReadings
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b2f7fc620d5b401a.htm#ID_aaa1f504faadc83a0a00206a00d10cf3-900c4040faadc28d0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "PMReadings"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class RRECeiver(SCPINode, SCPIBool):
                        """
                        SOURce:POWer:CORRection:COLLect:RRECeiver
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "RRECeiver"
                        args = ["1", "OFF", "ON"]
                        
                class DATA(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:DATA
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/25fbcbae02e24593.htm#ID_b9bdd113faade6230a00206a0169b185-c18fca3afaade0660a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "DATA"
                    args = ["'string'"]
                    
                    class PARameter(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:DATA:PARameter
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5e0229cc7b574769.htm#ID_8e7c1329e2b4ffc60a002019006b50ba-25446696e2b4fe8d0a002019017b841c-en-US>`_
                        
                        Arguments: ATTenuation, CFRequency, CPOWer, FSMode, LTSTamp, MTESt, MVNA, POINts, STARt, STOP, STYPe, TSTamp, TVNA, WAVE
                        """
                        _cmd = "PARameter"
                        args = ["ATTenuation", "CFRequency", "CPOWer", "FSMode", "LTSTamp", "MTESt", "MVNA", "POINts", "STARt", "STOP", "STYPe", "TSTamp", "TVNA", "WAVE"]
                        
                        class COUNt(SCPINode, SCPIQuery):
                            """
                            `SOURce:POWer:CORRection:DATA:PARameter:COUNt
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0a721461bb424f11.htm#ID_09e9ca8be2b5015c0a00201900f8311e-9e62e375e2b500240a002019017b841c-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "COUNt"
                            args = [""]
                            
                    class PORT(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:DATA:PORT
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/25fbcbae02e24593.htm#ID_a272ee70351562700a00206a00303ef7-9a74021135155b2c0a00206a01f2dc17-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "PORT"
                        args = ["'string'"]
                        
                class DEFault(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:CORRection:DEFault
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "DEFault"
                    args = ["1", "OFF", "ON"]
                    
                class FAST(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:CORRection:FAST
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "FAST"
                    args = ["1", "OFF", "ON"]
                    
                class GENerator(SCPINodeN, SCPIBool):
                    """
                    SOURce:POWer:CORRection:GENerator
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "GENerator"
                    args = ["1", "OFF", "ON"]
                    
                    class LEVel(SCPINode):
                        """
                        SOURce:POWer:CORRection:GENerator:LEVel
                        
                        Arguments: 
                        """
                        _cmd = "LEVel"
                        args = [""]
                        
                        class OFFSet(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:GENerator:LEVel:OFFSet
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0eb4b6bdcf0d4e21.htm#ID_abb96447faadfcd70a00206a018d0552-297bb390faadf6eb0a00206a01a6673d-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "OFFSet"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:CORRection:GENerator:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e9de207841044de6.htm#ID_fa7913e6faae04490a00206a01792c96-0729a476faadfebb0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class HARMonic(SCPINode, SCPISet):
                    """
                    SOURce:POWer:CORRection:HARMonic
                    
                    Arguments: 
                    """
                    _cmd = "HARMonic"
                    args = [""]
                    
                    class ACQuire(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:HARMonic:ACQuire
                        
                        Arguments: 
                        """
                        _cmd = "ACQuire"
                        args = [""]
                        
                class IMODulation(SCPINode):
                    """
                    SOURce:POWer:CORRection:IMODulation
                    
                    Arguments: 
                    """
                    _cmd = "IMODulation"
                    args = [""]
                    
                    class LTONe(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:IMODulation:LTONe
                        
                        Arguments: 
                        """
                        _cmd = "LTONe"
                        args = [""]
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:IMODulation:LTONe:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d3ff622b7a56411d.htm#ID_bb03f965faae136c0a00206a00c59a89-d9aa326efaae0da00a00206a01a6673d-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "ACQuire"
                            args = [""]
                            
                    class PORT(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:IMODulation:PORT
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/41a0d5a57dba437b.htm#ID_2248f3c0bba91b3d0a00201900e05938-b5e967b0bba91a140a0020190170f726-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "PORT"
                        args = ["'string'"]
                        
                    class UTONe(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:IMODulation:UTONe
                        
                        Arguments: 
                        """
                        _cmd = "UTONe"
                        args = [""]
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:IMODulation:UTONe:ACQuire
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5d8d28cae0ee4ec7.htm#ID_4887b100faae1ade0a00206a01623c15-4f33d57bfaae15410a00206a01a6673d-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "ACQuire"
                            args = [""]
                            
                class LEVel(SCPINode):
                    """
                    SOURce:POWer:CORRection:LEVel
                    
                    Arguments: 
                    """
                    _cmd = "LEVel"
                    args = [""]
                    
                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:LEVel:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/25ace39a40ac49b1.htm#ID_00e3bf8afaae22800a00206a00b4aa09-059f33b0faae1cb30a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "OFFSet"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class MIXer(SCPINode):
                    """
                    SOURce:POWer:CORRection:MIXer
                    
                    Arguments: 
                    """
                    _cmd = "MIXer"
                    args = [""]
                    
                    class IF(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:MIXer:IF
                        
                        Arguments: 
                        """
                        _cmd = "IF"
                        args = [""]
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            SOURce:POWer:CORRection:MIXer:IF:ACQuire
                            
                            Arguments: 
                            """
                            _cmd = "ACQuire"
                            args = [""]
                            
                    class LO(SCPINodeN, SCPISet):
                        """
                        SOURce:POWer:CORRection:MIXer:LO
                        
                        Arguments: 
                        """
                        _cmd = "LO"
                        args = [""]
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            SOURce:POWer:CORRection:MIXer:LO:ACQuire
                            
                            Arguments: 
                            """
                            _cmd = "ACQuire"
                            args = [""]
                            
                    class RF(SCPINode, SCPISet):
                        """
                        SOURce:POWer:CORRection:MIXer:RF
                        
                        Arguments: 
                        """
                        _cmd = "RF"
                        args = [""]
                        
                        class ACQuire(SCPINode, SCPISet):
                            """
                            SOURce:POWer:CORRection:MIXer:RF:ACQuire
                            
                            Arguments: 
                            """
                            _cmd = "ACQuire"
                            args = [""]
                            
                class NREadings(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:NREadings
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0ca09ffe643247a6.htm#ID_dec18885faae40580a00206a016a7cf9-b9a1534efaae3aca0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "NREadings"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class OSOurces(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:CORRection:OSOurces
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "OSOurces"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:CORRection:OSOurces:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9d8512972ee64ae5.htm#ID_3b3d0ddbfaae47f90a00206a018e9655-fcf684aefaae424c0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class PMETer(SCPINode):
                    """
                    SOURce:POWer:CORRection:PMETer
                    
                    Arguments: 
                    """
                    _cmd = "PMETer"
                    args = [""]
                    
                    class ID(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:PMETer:ID
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e115480.htm#ID_718458d9faae4fd90a00206a014851d1-3e93700cfaae49ce0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "ID"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class PPOWer(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:PPOWer
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c5a8849efde0475a.htm#ID_b404743a3515a4a80a00206a014bce76-c8cda1ef351598740a00206a01f2dc17-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "PPOWer"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class PSELect(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:CORRection:PSELect
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/72023c98c65e447f.htm#ID_b7cb46713515b2e10a00206a00ab5074-98441fc73515aad30a00206a01f2dc17-en-US>`_
                    
                    Arguments: CPOWer, PPOWer
                    """
                    _cmd = "PSELect"
                    args = ["CPOWer", "PPOWer"]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:CORRection:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dec754a87b374b92.htm#ID_aba4178bfaae57890a00206a00e59888-88fe3b6afaae51dc0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
                class TCOefficient(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:CORRection:TCOefficient
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "TCOefficient"
                    args = ["1", "OFF", "ON"]
                    
                    class CALibration(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:CALibration
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/082d754c7e824b9e.htm#ID_ae42fb54612b11db0a00206a0127a802-26ad09a8612b05480a00206a01ed2866-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "CALibration"
                        args = ["1", "OFF", "ON"]
                        
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:COUNt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7467446d7bc7431b.htm#ID_173a4efd612b22460a00206a00ef257c-74e014cb612b15360a00206a01ed2866-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "COUNt"
                        args = [""]
                        
                    class DEFine(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:DEFine
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/03d957429191480b.htm#ID_bda67605612b2f270a00206a01114ab4-aca50f20612b27470a00206a01ed2866-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "DEFine"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class DELete(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:CORRection:TCOefficient:DELete
                        
                        Arguments: 
                        """
                        _cmd = "DELete"
                        args = [""]
                        
                        class ALL(SCPINode, SCPISet):
                            """
                            `SOURce:POWer:CORRection:TCOefficient:DELete:ALL
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cf97363339154f86.htm#ID_9ef00398612b3c850a00206a00866808-d704ff41612b32340a00206a01ed2866-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "ALL"
                            args = [""]
                            
                        class DUMMy(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SOURce:POWer:CORRection:TCOefficient:DELete:DUMMy
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2fbf785d99684f5f.htm#ID_f913fc5b612b483d0a00206a01410ab5-a060a1a1612b3ff00a00206a01ed2866-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "DUMMy"
                            args = [""]
                            
                    class FEED(SCPINode, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:FEED
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7d96b4dfe19e4c9b.htm#ID_d8cc63b3612b525e0a00206a01d7a7c3-3305d9e8612b4a9e0a00206a01ed2866-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "FEED"
                        args = ["'string'"]
                        
                    class INSert(SCPINodeN, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:INSert
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a7514edfae9d4a97.htm#ID_237311af612b5dd80a00206a003289ba-eeed4680612b558b0a00206a01ed2866-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "INSert"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:CORRection:TCOefficient:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2cc602d287784c4e.htm#ID_8bd9cb78612b69510a00206a01eabac8-91600e8e612b60870a00206a01ed2866-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
            class COUPle(SCPINode, SCPIBool):
                """
                SOURce:POWer:COUPle
                
                Arguments: 1, OFF, ON
                """
                _cmd = "COUPle"
                args = ["1", "OFF", "ON"]
                
            class GENerator(SCPINodeN):
                """
                SOURce:POWer:GENerator
                
                Arguments: 
                """
                _cmd = "GENerator"
                args = [""]
                
                class LLIMit(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:GENerator:LLIMit
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "LLIMit"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        SOURce:POWer:GENerator:LLIMit:STATe
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                    class VALue(SCPINode, SCPIQuery, SCPISet):
                        """
                        SOURce:POWer:GENerator:LLIMit:VALue
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "VALue"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class OFFSet(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:GENerator:OFFSet
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bf9688b40fbb4ac9.htm#ID_117aa5bafaae857f0a00206a002f271a-e6a66decfaae7fb30a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "OFFSet"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class PERManent(SCPINode, SCPIBool):
                    """
                    SOURce:POWer:GENerator:PERManent
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "PERManent"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SOURce:POWer:GENerator:PERManent:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/29150ecf191b40c9.htm#ID_11c0b55efaae8d9d0a00206a01b64dae-cda894d1faae87730a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:GENerator:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2b2ef3243ae24a58.htm#ID_0269c345faae950f0a00206a011daa70-fee7be52faae8f810a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class LEVel(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:POWer:LEVel
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "LEVel"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class IMMediate(SCPINode, SCPIQuery, SCPISet):
                    """
                    SOURce:POWer:LEVel:IMMediate
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "IMMediate"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                    class AMPLitude(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:AMPLitude
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cb0449cb743f4614.htm#ID_d19e984efaaef0ac0a00206a0031e7ac-96acb6e3faaeeb1e0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "AMPLitude"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class LLIMit(SCPINode, SCPIBool):
                        """
                        SOURce:POWer:LEVel:IMMediate:LLIMit
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "LLIMit"
                        args = ["1", "OFF", "ON"]
                        
                        class DGRaccess(SCPINode, SCPIBool):
                            """
                            SOURce:POWer:LEVel:IMMediate:LLIMit:DGRaccess
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "DGRaccess"
                            args = ["1", "OFF", "ON"]
                            
                        class STATe(SCPINode, SCPIBool):
                            """
                            SOURce:POWer:LEVel:IMMediate:LLIMit:STATe
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                        class VALue(SCPINode, SCPIQuery, SCPISet):
                            """
                            SOURce:POWer:LEVel:IMMediate:LLIMit:VALue
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "VALue"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                    class OFFSet(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:OFFSet
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d163782716654728.htm#ID_abfaa0e1faaed2b40a00206a00aa2a79-e7e8f447faaeccd80a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "OFFSet"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                    class SLOPe(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SOURce:POWer:LEVel:IMMediate:SLOPe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6a3b406f0df84e3b.htm#ID_d01551b2faaee1b80a00206a0027f573-f0a6fd8cfaaedc2a0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "SLOPe"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                        class STATe(SCPINode, SCPIBool):
                            """
                            SOURce:POWer:LEVel:IMMediate:SLOPe:STATe
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
            class PERManent(SCPINode, SCPIBool):
                """
                SOURce:POWer:PERManent
                
                Arguments: 1, OFF, ON
                """
                _cmd = "PERManent"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:PERManent:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4a52786e213a4377.htm#ID_33dd3b36faae9cc00a00206a01124b41-a709680bfaae97030a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class REDuce(SCPINode, SCPIBool):
                """
                SOURce:POWer:REDuce
                
                Arguments: 1, OFF, ON
                """
                _cmd = "REDuce"
                args = ["1", "OFF", "ON"]
                
                class SDELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:REDuce:SDELay
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/76c24730662a4cc6.htm#ID_ad5bec09b7ffa5770a001ae7253f904c-2ad64f47b7ffa42e0a001ae732f546b3-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "SDELay"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `SOURce:POWer:REDuce:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/390210369fef483e.htm#ID_da2ac181b7ffa7990a001ae722723f79-9010cb6db7ffa6420a001ae732f546b3-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class STARt(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:STARt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2facbd33341b4107.htm#ID_4899138ffaaea4800a00206a01efb643-73d350bafaae9ea40a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "STARt"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class STATe(SCPINode, SCPIBool):
                """
                `SOURce:POWer:STATe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/64db3d3b774d43db.htm#ID_628e8e9bfaaeac210a00206a00f0e1b9-ac3408ddfaaea6550a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATe"
                args = ["1", "OFF", "ON"]
                
            class STOP(SCPINode, SCPIQuery, SCPISet):
                """
                `SOURce:POWer:STOP
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2facbd33341b4107.htm#ID_f96cb7dbfaaeb4110a00206a01447348-2719bf89faaeae150a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "STOP"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class SWEepend(SCPINode):
                """
                SOURce:POWer:SWEepend
                
                Arguments: 
                """
                _cmd = "SWEepend"
                args = [""]
                
                class MODE(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:SWEepend:MODE
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9b72458c45a44cab.htm#ID_04ee670042b0cba40a001ae71571ea53-eeac341142b0c8f40a001ae769a5b4da-en-US>`_
                    
                    Arguments: AUTO, KEEP, REDuce
                    """
                    _cmd = "MODE"
                    args = ["AUTO", "KEEP", "REDuce"]
                    
                class SDELay(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SOURce:POWer:SWEepend:SDELay
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0e8fcd86e44c4c30.htm#ID_60a3fe9e42b0cda70a001ae736ba83e3-ea985cc442b0cc300a001ae769a5b4da-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "SDELay"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
        class TDIF(SCPINode):
            """
            SOURce:TDIF
            
            Arguments: 
            """
            _cmd = "TDIF"
            args = [""]
            
            class WAVes(SCPINode, SCPIQuery, SCPISet):
                """
                SOURce:TDIF:WAVes
                
                Arguments: DCMode, SENDed
                """
                _cmd = "WAVes"
                args = ["DCMode", "SENDed"]
                
    class STATus(SCPINode):
        """
        STATus
        
        Arguments: 
        """
        _cmd = "STATus"
        args = [""]
        
        class OPERation(SCPINode, SCPIQuery, SCPISet):
            """
            STATus:OPERation
            
            Arguments: 
            """
            _cmd = "OPERation"
            args = [""]
            
            class CONDition(SCPINode, SCPIQuery):
                """
                STATus:OPERation:CONDition
                
                Arguments: 
                """
                _cmd = "CONDition"
                args = [""]
                
            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:ENABle
                
                Arguments: 1
                """
                _cmd = "ENABle"
                args = ["1"]
                
            class EVENt(SCPINode, SCPIQuery):
                """
                STATus:OPERation:EVENt
                
                Arguments: 
                """
                _cmd = "EVENt"
                args = [""]
                
            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:NTRansition
                
                Arguments: 1
                """
                _cmd = "NTRansition"
                args = ["1"]
                
            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:OPERation:PTRansition
                
                Arguments: 1
                """
                _cmd = "PTRansition"
                args = ["1"]
                
        class PRESet(SCPINode, SCPISet):
            """
            `STATus:PRESet
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e117466.htm#ID_14990f1cfaaf5cf30a00206a01af2d38-6dc6fe51faaf57740a00206a01a6673d-en-US>`_
            
            Arguments: 
            """
            _cmd = "PRESet"
            args = [""]
            
        class QUEStionable(SCPINode, SCPIQuery, SCPISet):
            """
            STATus:QUEStionable
            
            Arguments: 
            """
            _cmd = "QUEStionable"
            args = [""]
            
            class CONDition(SCPINode, SCPIQuery):
                """
                `STATus:QUEStionable:CONDition
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/acf0533fb1e4434e.htm#ID_ec46ac9afaaf64a30a00206a00c8bf13-aaf5fdf0faaf5ef60a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "CONDition"
                args = [""]
                
            class ENABle(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:ENABle
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/165d9083d7514744.htm#ID_cb2fe2bcfaaf6c250a00206a002a52d7-12884f3ffaaf66880a00206a01a6673d-en-US>`_
                
                Arguments: 1
                """
                _cmd = "ENABle"
                args = ["1"]
                
            class EVENt(SCPINode, SCPIQuery):
                """
                `STATus:QUEStionable:EVENt
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/edbdffb720be4c72.htm#ID_85f7b6b5faaff47f0a00206a00265edf-50127a48faafeed20a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "EVENt"
                args = [""]
                
            class INTegrity(SCPINode, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:INTegrity
                
                Arguments: 
                """
                _cmd = "INTegrity"
                args = [""]
                
                class CONDition(SCPINode, SCPIQuery):
                    """
                    `STATus:QUEStionable:INTegrity:CONDition
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/acf0533fb1e4434e.htm#ID_0333fbe8faaf73a70a00206a013b59a3-26dc522ffaaf6e090a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "CONDition"
                    args = [""]
                    
                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:INTegrity:ENABle
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/165d9083d7514744.htm#ID_3aabbef6faaf7b380a00206a01a6dac4-c217b852faaf757c0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]
                    
                class EVENt(SCPINode, SCPIQuery):
                    """
                    `STATus:QUEStionable:INTegrity:EVENt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/edbdffb720be4c72.htm#ID_4cda7716faafb7a50a00206a0059dcea-fe65ae3cfaafb1e80a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "EVENt"
                    args = [""]
                    
                class HARDware(SCPINode, SCPIQuery, SCPISet):
                    """
                    STATus:QUEStionable:INTegrity:HARDware
                    
                    Arguments: 
                    """
                    _cmd = "HARDware"
                    args = [""]
                    
                    class CONDition(SCPINode, SCPIQuery):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:CONDition
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/acf0533fb1e4434e.htm#ID_31ec8179faaf82ab0a00206a01399c5a-48b257acfaaf7d1d0a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "CONDition"
                        args = [""]
                        
                    class ENABle(SCPINode, SCPIQuery, SCPISet):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:ENABle
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/165d9083d7514744.htm#ID_e278e1cafaaf8a4c0a00206a00eea680-6bd338a7faaf847f0a00206a01a6673d-en-US>`_
                        
                        Arguments: 1
                        """
                        _cmd = "ENABle"
                        args = ["1"]
                        
                    class EVENt(SCPINode, SCPIQuery):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:EVENt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/edbdffb720be4c72.htm#ID_7c9f00d6faafa0d10a00206a017c8e51-d642c8f9faaf9b530a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "EVENt"
                        args = [""]
                        
                    class NTRansition(SCPINode, SCPIQuery, SCPISet):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:NTRansition
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8b6b137e86d7462f.htm#ID_2a6cb24efaaf91ce0a00206a001b46d6-3974f3f9faaf8c200a00206a01a6673d-en-US>`_
                        
                        Arguments: 1
                        """
                        _cmd = "NTRansition"
                        args = ["1"]
                        
                    class PTRansition(SCPINode, SCPIQuery, SCPISet):
                        """
                        `STATus:QUEStionable:INTegrity:HARDware:PTRansition
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1bf60bca7cd4485b.htm#ID_00ec2fb7faaf996f0a00206a00babf2b-227ed9b6faaf93a20a00206a01a6673d-en-US>`_
                        
                        Arguments: 1
                        """
                        _cmd = "PTRansition"
                        args = ["1"]
                        
                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:INTegrity:NTRansition
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8b6b137e86d7462f.htm#ID_4838dc31faafa8920a00206a013b68fd-a0b93b62faafa2d50a00206a01a6673d-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]
                    
                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:INTegrity:PTRansition
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1bf60bca7cd4485b.htm#ID_34bab32dfaafb0040a00206a01d13a50-6dab1c20faafaa760a00206a01a6673d-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]
                    
            class LIMit(SCPINodeN, SCPIQuery, SCPISet):
                """
                STATus:QUEStionable:LIMit
                
                Arguments: 
                """
                _cmd = "LIMit"
                args = [""]
                
                class CONDition(SCPINode, SCPIQuery):
                    """
                    `STATus:QUEStionable:LIMit:CONDition
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/acf0533fb1e4434e.htm#ID_9ce66863faafbf460a00206a018efcc8-ad923fe4faafb97a0a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "CONDition"
                    args = [""]
                    
                class ENABle(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:LIMit:ENABle
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/165d9083d7514744.htm#ID_ad66516bfaafc6d80a00206a0177398d-8207f46ffaafc13a0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "ENABle"
                    args = ["1"]
                    
                class EVENt(SCPINode, SCPIQuery):
                    """
                    `STATus:QUEStionable:LIMit:EVENt
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/edbdffb720be4c72.htm#ID_f07789a5faafddda0a00206a0084664d-c2d70464faafd82d0a00206a01a6673d-en-US>`_
                    
                    Arguments: 
                    """
                    _cmd = "EVENt"
                    args = [""]
                    
                class NTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:LIMit:NTRansition
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8b6b137e86d7462f.htm#ID_1f6cf0c8faafce690a00206a00e85b2c-52051c71faafc8bc0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "NTRansition"
                    args = ["1"]
                    
                class PTRansition(SCPINode, SCPIQuery, SCPISet):
                    """
                    `STATus:QUEStionable:LIMit:PTRansition
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1bf60bca7cd4485b.htm#ID_5f3a5c1dfaafd60a0a00206a00b66faf-afc7fac9faafd04d0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1
                    """
                    _cmd = "PTRansition"
                    args = ["1"]
                    
            class NTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:NTRansition
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8b6b137e86d7462f.htm#ID_5f4b6776faafe57b0a00206a008aebef-2ecf6d87faafdfce0a00206a01a6673d-en-US>`_
                
                Arguments: 1
                """
                _cmd = "NTRansition"
                args = ["1"]
                
            class PTRansition(SCPINode, SCPIQuery, SCPISet):
                """
                `STATus:QUEStionable:PTRansition
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1bf60bca7cd4485b.htm#ID_135540eafaafecfd0a00206a009c969a-29d24063faafe7500a00206a01a6673d-en-US>`_
                
                Arguments: 1
                """
                _cmd = "PTRansition"
                args = ["1"]
                
        class QUEue(SCPINode, SCPIQuery, SCPISet):
            """
            STATus:QUEue
            
            Arguments: 
            """
            _cmd = "QUEue"
            args = [""]
            
            class NEXT(SCPINode, SCPIQuery):
                """
                `STATus:QUEue:NEXT
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e118240.htm#ID_3d4f47acfaaffc300a00206a0013451f-0611f439faaff6630a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "NEXT"
                args = [""]
                
    class SYSTem(SCPINode):
        """
        SYSTem
        
        Arguments: 
        """
        _cmd = "SYSTem"
        args = [""]
        
        class COMMunicate(SCPINode):
            """
            SYSTem:COMMunicate
            
            Arguments: 
            """
            _cmd = "COMMunicate"
            args = [""]
            
            class AKAL(SCPINode):
                """
                SYSTem:COMMunicate:AKAL
                
                Arguments: 
                """
                _cmd = "AKAL"
                args = [""]
                
                class CONNection(SCPINode, SCPISet):
                    """
                    `SYSTem:COMMunicate:AKAL:CONNection
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e118291.htm#ID_b6e9a9a2fab003a20a00206a016cc0b8-27c8d699faaffe040a00206a01a6673d-en-US>`_
                    
                    Arguments: MATCh, OPEN, SHORt, THRough
                    """
                    _cmd = "CONNection"
                    args = ["MATCh", "OPEN", "SHORt", "THRough"]
                    
                class MMEMory(SCPINode, SCPIBool):
                    """
                    SYSTem:COMMunicate:AKAL:MMEMory
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "MMEMory"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SYSTem:COMMunicate:AKAL:MMEMory:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e118337.htm#ID_34916594fab00b430a00206a0082898c-7dad1344fab005860a00206a01a6673d-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
            class CODec(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:COMMunicate:CODec
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1052114e59e64095.htm#ID_696257e66f679a250a001ae70ec75580-d27074166f6798ae0a001ae727f5f310-en-US>`_
                
                Arguments: ASCii, SJIS, UTF8
                """
                _cmd = "CODec"
                args = ["ASCii", "SJIS", "UTF8"]
                
            class GPIB(SCPINode):
                """
                SYSTem:COMMunicate:GPIB
                
                Arguments: 
                """
                _cmd = "GPIB"
                args = [""]
                
                class SELF(SCPINode):
                    """
                    SYSTem:COMMunicate:GPIB:SELF
                    
                    Arguments: 
                    """
                    _cmd = "SELF"
                    args = [""]
                    
                    class ADDRess(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:GPIB:SELF:ADDRess
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b3ba68fb72ee42d8.htm#ID_61513521fab012e40a00206a01da716c-2ddf570ffab00d270a00206a01a6673d-en-US>`_
                        
                        Arguments: 1
                        """
                        _cmd = "ADDRess"
                        args = ["1"]
                        
                    class INIT(SCPINode):
                        """
                        SYSTem:COMMunicate:GPIB:SELF:INIT
                        
                        Arguments: 
                        """
                        _cmd = "INIT"
                        args = [""]
                        
                        class WAIT(SCPINode, SCPIBool):
                            """
                            `SYSTem:COMMunicate:GPIB:SELF:INIT:WAIT
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/14a624620e7d44ab.htm#ID_68a7116fbe5215800a001ae738b88c4c-9d13e972be5213fa0a001ae76004eba8-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "WAIT"
                            args = ["1", "OFF", "ON"]
                            
                    class LPORt(SCPINode):
                        """
                        SYSTem:COMMunicate:GPIB:SELF:LPORt
                        
                        Arguments: 
                        """
                        _cmd = "LPORt"
                        args = [""]
                        
                        class ALIGn(SCPINode, SCPIBool):
                            """
                            `SYSTem:COMMunicate:GPIB:SELF:LPORt:ALIGn
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1fec17069a1a42e4.htm#ID_83ec9beebe5217a30a001ae728c4b621-64202eadbe52160d0a001ae76004eba8-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "ALIGn"
                            args = ["1", "OFF", "ON"]
                            
                    class RTERminator(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:GPIB:SELF:RTERminator
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e118521.htm#ID_ea61ddf3fab01a660a00206a01bf8be0-c5397efffab014c80a00206a01a6673d-en-US>`_
                        
                        Arguments: EOI, LFEoi
                        """
                        _cmd = "RTERminator"
                        args = ["EOI", "LFEoi"]
                        
            class INTernal(SCPINode):
                """
                SYSTem:COMMunicate:INTernal
                
                Arguments: 
                """
                _cmd = "INTernal"
                args = [""]
                
                class COMMand(SCPINode):
                    """
                    SYSTem:COMMunicate:INTernal:COMMand
                    
                    Arguments: 
                    """
                    _cmd = "COMMand"
                    args = [""]
                    
                    class TABLes(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:INTernal:COMMand:TABLes
                        
                        Arguments: 'string'
                        """
                        _cmd = "TABLes"
                        args = ["'string'"]
                        
                class REMote(SCPINode, SCPIBool):
                    """
                    SYSTem:COMMunicate:INTernal:REMote
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "REMote"
                    args = ["1", "OFF", "ON"]
                    
            class NET(SCPINode):
                """
                SYSTem:COMMunicate:NET
                
                Arguments: 
                """
                _cmd = "NET"
                args = [""]
                
                class HOSTname(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:COMMunicate:NET:HOSTname
                    
                    Arguments: 'string'
                    """
                    _cmd = "HOSTname"
                    args = ["'string'"]
                    
            class RDEVice(SCPINode):
                """
                SYSTem:COMMunicate:RDEVice
                
                Arguments: 
                """
                _cmd = "RDEVice"
                args = [""]
                
                class AKAL(SCPINodeN):
                    """
                    SYSTem:COMMunicate:RDEVice:AKAL
                    
                    Arguments: 
                    """
                    _cmd = "AKAL"
                    args = [""]
                    
                    class ADDRess(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:AKAL:ADDRess
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/7a0adfab1a314193.htm#ID_38ecc45ffab031490a00206a01f30588-bafade31fab02b9c0a00206a01a6673d-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "ADDRess"
                        args = ["'string'"]
                        
                        class ALL(SCPINode, SCPIQuery):
                            """
                            `SYSTem:COMMunicate:RDEVice:AKAL:ADDRess:ALL
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e118599.htm#ID_12b46c80fab038fa0a00206a00cf3f89-d294ec5bfab0332e0a00206a01a6673d-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "ALL"
                            args = [""]
                            
                    class CATalog(SCPINode, SCPIQuery):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:CATalog
                        
                        Arguments: 
                        """
                        _cmd = "CATalog"
                        args = [""]
                        
                    class CKIT(SCPINode):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:CKIT
                        
                        Arguments: 
                        """
                        _cmd = "CKIT"
                        args = [""]
                        
                        class CATalog(SCPINode, SCPIQuery):
                            """
                            `SYSTem:COMMunicate:RDEVice:AKAL:CKIT:CATalog
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/321d1d0427e343bf.htm#ID_e2b55a2491e0e9db0a00206a00224e9a-50e93f0f91e0dc6d0a00206a00e9ecac-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "CATalog"
                            args = [""]
                            
                        class STANdard(SCPINode):
                            """
                            SYSTem:COMMunicate:RDEVice:AKAL:CKIT:STANdard
                            
                            Arguments: 
                            """
                            _cmd = "STANdard"
                            args = [""]
                            
                            class CATalog(SCPINode, SCPIQuery, SCPISet):
                                """
                                `SYSTem:COMMunicate:RDEVice:AKAL:CKIT:STANdard:CATalog
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/86aba03e3ec94134.htm#ID_ed1982c535163ef40a00206a01459e8b-5354b0a4351637530a00206a01f2dc17-en-US>`_
                                
                                Arguments: 'string'
                                """
                                _cmd = "CATalog"
                                args = ["'string'"]
                                
                    class CONFigure(SCPINode):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:CONFigure
                        
                        Arguments: 
                        """
                        _cmd = "CONFigure"
                        args = [""]
                        
                        class AUTO(SCPINode, SCPIBool):
                            """
                            SYSTem:COMMunicate:RDEVice:AKAL:CONFigure:AUTO
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "AUTO"
                            args = ["1", "OFF", "ON"]
                            
                            class STATe(SCPINode, SCPIBool):
                                """
                                SYSTem:COMMunicate:RDEVice:AKAL:CONFigure:AUTO:STATe
                                
                                Arguments: 1, OFF, ON
                                """
                                _cmd = "STATe"
                                args = ["1", "OFF", "ON"]
                                
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:COUNt
                        
                        Arguments: 
                        """
                        _cmd = "COUNt"
                        args = [""]
                        
                    class DATE(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:AKAL:DATE
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/26a325509010424f.htm#ID_0a954ea791e0f9b90a00206a01b9cb3d-092c4e9f91e0f14d0a00206a00e9ecac-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "DATE"
                        args = ["'string'"]
                        
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:DEFine
                        
                        Arguments: 'string'
                        """
                        _cmd = "DEFine"
                        args = ["'string'"]
                        
                    class DELete(SCPINode, SCPISet):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:DELete
                        
                        Arguments: 
                        """
                        _cmd = "DELete"
                        args = [""]
                        
                    class FRANge(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:AKAL:FRANge
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2fe4d725e67f40c2.htm#ID_227c868091e1035e0a00206a00808933-f810ee9a91e0fc4a0a00206a00e9ecac-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "FRANge"
                        args = ["'string'"]
                        
                    class PORTs(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:AKAL:PORTs
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5257accae9324f22.htm#ID_9298113091e10ee70a00206a01d92f21-f852f2d391e105b00a00206a00e9ecac-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "PORTs"
                        args = ["'string'"]
                        
                    class PREDuction(SCPINode, SCPIBool):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:PREDuction
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "PREDuction"
                        args = ["1", "OFF", "ON"]
                        
                        class STATe(SCPINode, SCPIBool):
                            """
                            `SYSTem:COMMunicate:RDEVice:AKAL:PREDuction:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e118850.htm#ID_79a5e788e15d18260a00206a0144c9a6-aa8db572e15d11020a00206a00796295-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                    class SDATa(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:AKAL:SDATa
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bedef83f5a58483f.htm#ID_8962fa362b9c026c0a00206a01432b9a-c7df0c252b9bfb280a00206a0020d3a0-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "SDATa"
                        args = ["'string'"]
                        
                    class WARMup(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:RDEVice:AKAL:WARMup
                        
                        Arguments: 
                        """
                        _cmd = "WARMup"
                        args = [""]
                        
                        class STATe(SCPINode, SCPIQuery):
                            """
                            `SYSTem:COMMunicate:RDEVice:AKAL:WARMup:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e118968.htm#ID_276e3c1791e11bb80a00206a01ac5dc5-a50c9ce891e1132d0a00206a00e9ecac-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "STATe"
                            args = [""]
                            
                class GENerator(SCPINodeN):
                    """
                    SYSTem:COMMunicate:RDEVice:GENerator
                    
                    Arguments: 
                    """
                    _cmd = "GENerator"
                    args = [""]
                    
                    class CATalog(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:CATalog
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0aec52e1cf544e09.htm#ID_632db67afab04fbe0a00206a01429d80-e640b520fab04a200a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "CATalog"
                        args = [""]
                        
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:COUNt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e119049.htm#ID_3b5eb98efab0578e0a00206a017a57f7-77203d8ffab051d10a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "COUNt"
                        args = [""]
                        
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:DEFine
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8142ad99eab840e8.htm#ID_00159b1efab05f1f0a00206a01cbbccc-ec8148fbfab059820a00206a01a6673d-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "DEFine"
                        args = ["'string'"]
                        
                    class DELete(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:DELete
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e118999.htm#ID_96c9fc01fab066ff0a00206a00727635-ee59ffa2fab061620a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "DELete"
                        args = [""]
                        
                    class SEPMode(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:SEPMode
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a02e1397662d4b37.htm#ID_e2afc1d3e15d34390a00206a01d9fc25-db7b4172e15d2c980a00206a00796295-en-US>`_
                        
                        Arguments: KEEP, LOW, OFF, USER
                        """
                        _cmd = "SEPMode"
                        args = ["KEEP", "LOW", "OFF", "USER"]
                        
                    class SEPower(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:GENerator:SEPower
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/1fea9e339d68455f.htm#ID_33d0b7dde15d40ad0a00206a017d2253-032c215fe15d37560a00206a00796295-en-US>`_
                        
                        Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                        """
                        _cmd = "SEPower"
                        args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                        
                class PMETer(SCPINodeN):
                    """
                    SYSTem:COMMunicate:RDEVice:PMETer
                    
                    Arguments: 
                    """
                    _cmd = "PMETer"
                    args = [""]
                    
                    class AZERo(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:AZERo
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/b47f04ba45f847b5.htm#ID_96b8e93efab06e710a00206a00ed7fa9-634f7de2fab068e30a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "AZERo"
                        args = [""]
                        
                    class CATalog(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:CATalog
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4a3fa363c3e44dda.htm#ID_11d8c23afab075f30a00206a007d910e-eda7f0a9fab070560a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "CATalog"
                        args = [""]
                        
                    class CONFigure(SCPINode):
                        """
                        SYSTem:COMMunicate:RDEVice:PMETer:CONFigure
                        
                        Arguments: 
                        """
                        _cmd = "CONFigure"
                        args = [""]
                        
                        class AUTO(SCPINode, SCPIBool):
                            """
                            SYSTem:COMMunicate:RDEVice:PMETer:CONFigure:AUTO
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "AUTO"
                            args = ["1", "OFF", "ON"]
                            
                            class STATe(SCPINode, SCPIBool):
                                """
                                `SYSTem:COMMunicate:RDEVice:PMETer:CONFigure:AUTO:STATe
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/5c3b3eaf608c4732.htm#ID_42018499fab07d850a00206a006d6b96-ccc5bc80fab077d70a00206a01a6673d-en-US>`_
                                
                                Arguments: 1, OFF, ON
                                """
                                _cmd = "STATe"
                                args = ["1", "OFF", "ON"]
                                
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:COUNt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e119413.htm#ID_86a7eabafab085350a00206a00f99a37-d17da2c6fab07f690a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "COUNt"
                        args = [""]
                        
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:DEFine
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/84bc325dc8a24407.htm#ID_f257effbfab08d050a00206a01c0972c-3e7d50f1fab0871a0a00206a01a6673d-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "DEFine"
                        args = ["'string'"]
                        
                    class DELete(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:PMETer:DELete
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e119331.htm#ID_163a5ca7fab094870a00206a00ff0043-f41c5122fab08eea0a00206a01a6673d-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "DELete"
                        args = [""]
                        
                    class SPCorrection(SCPINode, SCPIBool):
                        """
                        SYSTem:COMMunicate:RDEVice:PMETer:SPCorrection
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "SPCorrection"
                        args = ["1", "OFF", "ON"]
                        
                        class STATe(SCPINode, SCPIBool):
                            """
                            `SYSTem:COMMunicate:RDEVice:PMETer:SPCorrection:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/abc28ee8793c4707.htm#ID_c30269e6e2b52a410a0020190063b2f1-4d844fb7e2b529080a002019017b841c-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
                class SMATrix(SCPINodeN):
                    """
                    SYSTem:COMMunicate:RDEVice:SMATrix
                    
                    Arguments: 
                    """
                    _cmd = "SMATrix"
                    args = [""]
                    
                    class CATalog(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:SMATrix:CATalog
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/78b19041e1da4d8c.htm#ID_c527b777e2b52c160a002019003c8932-17f21d0de2b52aae0a002019017b841c-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "CATalog"
                        args = [""]
                        
                    class COMMand(SCPINode, SCPIQuery, SCPISet):
                        """
                        SYSTem:COMMunicate:RDEVice:SMATrix:COMMand
                        
                        Arguments: 'string'
                        """
                        _cmd = "COMMand"
                        args = ["'string'"]
                        
                    class CONFigure(SCPINode):
                        """
                        SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure
                        
                        Arguments: 
                        """
                        _cmd = "CONFigure"
                        args = [""]
                        
                        class ABORt(SCPINode, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:ABORt
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d864d14525904f3c.htm#ID_5af1ecc5e2b52f810a00201900488d61-917bd8cbe2b52e390a002019017b841c-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "ABORt"
                            args = [""]
                            
                        class END(SCPINode, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:END
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4ef25b4306be4226.htm#ID_2a271d6ee2b531460a002019017a6c38-50ea7940e2b52fee0a002019017b841c-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "END"
                            args = [""]
                            
                        class MLTest(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:MLTest
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/35615f2b64f146bc.htm#ID_bab31821e2b534a10a00201900a1c622-7726b90fe2b533780a002019017b841c-en-US>`_
                            
                            Arguments: 'string'
                            """
                            _cmd = "MLTest"
                            args = ["'string'"]
                            
                        class MLVNa(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:MLVNa
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/424e6d88914a4f4d.htm#ID_9d5ed720e2b536470a002019014fc067-cea1e85ce2b5350f0a002019017b841c-en-US>`_
                            
                            Arguments: 'string'
                            """
                            _cmd = "MLVNa"
                            args = ["'string'"]
                            
                        class MTESt(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:MTESt
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e120084.htm#ID_02dd88c3e2b5384b0a00201900a1ec16-5e68904ee2b537120a002019017b841c-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "MTESt"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class MVNA(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:MVNA
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e119949.htm#ID_2e3b266be2b53a2f0a002019002c349a-fcb7090be2b538c80a002019017b841c-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "MVNA"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                        class STARt(SCPINode, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:STARt
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/fe47c0c30d1347f2.htm#ID_d606c1c2e2b53c620a002019016d84ea-1085e87be2b53adb0a002019017b841c-en-US>`_
                            
                            Arguments: 
                            """
                            _cmd = "STARt"
                            args = [""]
                            
                        class TVNA(SCPINode, SCPIQuery, SCPISet):
                            """
                            `SYSTem:COMMunicate:RDEVice:SMATrix:CONFigure:TVNA
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/dba8b46d76e64fa2.htm#ID_2e9f6208e2b53e170a002019008d85be-1778be60e2b53ccf0a002019017b841c-en-US>`_
                            
                            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                            """
                            _cmd = "TVNA"
                            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                            
                    class COUNt(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:SMATrix:COUNt
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/0a53245cd6704fd1.htm#ID_54a467ace2b53fad0a0020190120e772-95630382e2b53e840a002019017b841c-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "COUNt"
                        args = [""]
                        
                    class DEFine(SCPINode, SCPIQuery, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:SMATrix:DEFine
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/01e5d99f805e431f.htm#ID_7496e554e2b541820a00201900a038ef-bbd862bae2b5402a0a002019017b841c-en-US>`_
                        
                        Arguments: 'string'
                        """
                        _cmd = "DEFine"
                        args = ["'string'"]
                        
                    class DELete(SCPINode, SCPISet):
                        """
                        `SYSTem:COMMunicate:RDEVice:SMATrix:DELete
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2f34ce5940394635.htm#ID_78fa76a8e2b543380a00201900eaad26-32d0ac12e2b541ef0a002019017b841c-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "DELete"
                        args = [""]
                        
                    class RELays(SCPINode):
                        """
                        SYSTem:COMMunicate:RDEVice:SMATrix:RELays
                        
                        Arguments: 
                        """
                        _cmd = "RELays"
                        args = [""]
                        
                        class SWITch(SCPINode):
                            """
                            SYSTem:COMMunicate:RDEVice:SMATrix:RELays:SWITch
                            
                            Arguments: 
                            """
                            _cmd = "SWITch"
                            args = [""]
                            
                            class COUNt(SCPINode, SCPIQuery):
                                """
                                `SYSTem:COMMunicate:RDEVice:SMATrix:RELays:SWITch:COUNt
                                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/203db75605364802.htm#ID_8464a0fa842f0b490a00201901538ecb-ed9ae3ce842f09c20a00201901936165-en-US>`_
                                
                                Arguments: 
                                """
                                _cmd = "COUNt"
                                args = [""]
                                
                    class SCAN(SCPINode, SCPIQuery):
                        """
                        `SYSTem:COMMunicate:RDEVice:SMATrix:SCAN
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bb5a2ce824f04a14.htm#ID_a5e70e1a42b0f6ac0a001ae702b3ea5d-4bc1954242b0f4d70a001ae769a5b4da-en-US>`_
                        
                        Arguments: 
                        """
                        _cmd = "SCAN"
                        args = [""]
                        
            class TCPip(SCPINode):
                """
                SYSTem:COMMunicate:TCPip
                
                Arguments: 
                """
                _cmd = "TCPip"
                args = [""]
                
                class CONTrol(SCPINode, SCPIQuery):
                    """
                    SYSTem:COMMunicate:TCPip:CONTrol
                    
                    Arguments: 
                    """
                    _cmd = "CONTrol"
                    args = [""]
                    
        class CORRection(SCPINode):
            """
            SYSTem:CORRection
            
            Arguments: 
            """
            _cmd = "CORRection"
            args = [""]
            
            class FMPort(SCPINode, SCPIBool):
                """
                SYSTem:CORRection:FMPort
                
                Arguments: 1, OFF, ON
                """
                _cmd = "FMPort"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    SYSTem:CORRection:FMPort:STATe
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class WIZard(SCPINode, SCPISet):
                """
                SYSTem:CORRection:WIZard
                
                Arguments: CKIT, MAIN
                """
                _cmd = "WIZard"
                args = ["CKIT", "MAIN"]
                
                class IMMediate(SCPINode, SCPISet):
                    """
                    `SYSTem:CORRection:WIZard:IMMediate
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/bb92d217236749cd.htm#ID_098763ae42b0f9e80a001ae71e064621-0f2c9abc42b0f8520a001ae769a5b4da-en-US>`_
                    
                    Arguments: CKIT, MAIN
                    """
                    _cmd = "IMMediate"
                    args = ["CKIT", "MAIN"]
                    
        class DATE(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:DATE
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/06074416ad144635.htm#ID_a847a1ebaaa8d6ac0a00206a006756f9-9b65deafaaa8cad50a00206a00dee6b8-en-US>`_
            
            Arguments: 1
            """
            _cmd = "DATE"
            args = ["1"]
            
        class DFPRint(SCPINode, SCPIQuery):
            """
            `SYSTem:DFPRint
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/16c0aaa4259448db.htm#ID_cae179f213575a160a00206a0180be6e-87f88bf6135754690a00206a0182dc26-en-US>`_
            
            Arguments: 
            """
            _cmd = "DFPRint"
            args = [""]
            
        class DISPlay(SCPINode):
            """
            SYSTem:DISPlay
            
            Arguments: 
            """
            _cmd = "DISPlay"
            args = [""]
            
            class BAR(SCPINode):
                """
                SYSTem:DISPlay:BAR
                
                Arguments: 
                """
                _cmd = "BAR"
                args = [""]
                
                class HKEY(SCPINode, SCPIBool):
                    """
                    SYSTem:DISPlay:BAR:HKEY
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "HKEY"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SYSTem:DISPlay:BAR:HKEY:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/04735c08c458471b.htm#ID_04b780c5a07057500a00206a010feb2c-f9cca7aaa070500c0a00206a013722ca-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class MENU(SCPINode, SCPIBool):
                    """
                    SYSTem:DISPlay:BAR:MENU
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "MENU"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SYSTem:DISPlay:BAR:MENU:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/04735c08c458471b.htm#ID_c7815f5ba07065d60a00206a01fcd35f-cee278d3a0705a1e0a00206a013722ca-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class STATus(SCPINode, SCPIBool):
                    """
                    SYSTem:DISPlay:BAR:STATus
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATus"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SYSTem:DISPlay:BAR:STATus:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/04735c08c458471b.htm#ID_7ceb2976a0706fc90a00206a01a03f62-0474fa26a07068960a00206a013722ca-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class STOols(SCPINode, SCPIBool):
                    """
                    SYSTem:DISPlay:BAR:STOols
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STOols"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SYSTem:DISPlay:BAR:STOols:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/04735c08c458471b.htm#ID_29ae8142a0707a0a0a00206a018e633e-0c0c26d3a070725a0a00206a013722ca-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class TITLe(SCPINode, SCPIBool):
                    """
                    SYSTem:DISPlay:BAR:TITLe
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "TITLe"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SYSTem:DISPlay:BAR:TITLe:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/04735c08c458471b.htm#ID_8e3e8248a07084c80a00206a014856cb-58386f94a0707ce90a00206a013722ca-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
                class TOOLs(SCPINode, SCPIBool):
                    """
                    SYSTem:DISPlay:BAR:TOOLs
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "TOOLs"
                    args = ["1", "OFF", "ON"]
                    
                    class STATe(SCPINode, SCPIBool):
                        """
                        `SYSTem:DISPlay:BAR:TOOLs:STATe
                        <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/04735c08c458471b.htm#ID_a45a5f24a0708fa60a00206a01841c0e-84805c29a07087780a00206a013722ca-en-US>`_
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "STATe"
                        args = ["1", "OFF", "ON"]
                        
            class COLor(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:DISPlay:COLor
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e120615.htm#ID_21c088fffab0b33a0a00206a01c816e7-d31ab677fab0ad9d0a00206a01a6673d-en-US>`_
                
                Arguments: BWLStyles, BWSolid, DBACkground, LBACkground
                """
                _cmd = "COLor"
                args = ["BWLStyles", "BWSolid", "DBACkground", "LBACkground"]
                
            class CONDuctances(SCPINode, SCPIBool):
                """
                `SYSTem:DISPlay:CONDuctances
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/47c43a4d53b54002.htm#ID_d2271c9397ea6f290a001ae77f4a7568-33a77b2097ea6de10a001ae760f7f904-en-US>`_
                
                Arguments: 1, OFF, ON
                """
                _cmd = "CONDuctances"
                args = ["1", "OFF", "ON"]
                
            class DIALogs(SCPINode):
                """
                SYSTem:DISPlay:DIALogs
                
                Arguments: 
                """
                _cmd = "DIALogs"
                args = [""]
                
                class SETup(SCPINode):
                    """
                    SYSTem:DISPlay:DIALogs:SETup
                    
                    Arguments: 
                    """
                    _cmd = "SETup"
                    args = [""]
                    
                    class MCAL(SCPINode, SCPIBool):
                        """
                        SYSTem:DISPlay:DIALogs:SETup:MCAL
                        
                        Arguments: 1, OFF, ON
                        """
                        _cmd = "MCAL"
                        args = ["1", "OFF", "ON"]
                        
                        class STATe(SCPINode, SCPIBool):
                            """
                            `SYSTem:DISPlay:DIALogs:SETup:MCAL:STATe
                            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/52e327a6f3ea4d29.htm#ID_617f4b3de2b548580a00201900ff0001-63b39231e2b547100a002019017b841c-en-US>`_
                            
                            Arguments: 1, OFF, ON
                            """
                            _cmd = "STATe"
                            args = ["1", "OFF", "ON"]
                            
            class UPDate(SCPINode, SCPIBool):
                """
                `SYSTem:DISPlay:UPDate
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e120670.htm#ID_4f17f97cfab0badb0a00206a019d73b8-482f9258fab0b53e0a00206a01a6673d-en-US>`_
                
                Arguments: 1, OFF, ON, ONCE
                """
                _cmd = "UPDate"
                args = ["1", "OFF", "ON", "ONCE"]
                
        class ERRor(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:ERRor
            
            Arguments: 
            """
            _cmd = "ERRor"
            args = [""]
            
            class ALL(SCPINode, SCPIQuery):
                """
                `SYSTem:ERRor:ALL
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e120712.htm#ID_3bd07848fab0c23e0a00206a01bf19dc-2c14d208fab0bcb00a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "ALL"
                args = [""]
                
            class DISPlay(SCPINode, SCPIBool):
                """
                SYSTem:ERRor:DISPlay
                
                Arguments: 1, OFF, ON
                """
                _cmd = "DISPlay"
                args = ["1", "OFF", "ON"]
                
                class ERRor(SCPINode, SCPIBool):
                    """
                    `SYSTem:ERRor:DISPlay:ERRor
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/089aa3644bc14e4a.htm#ID_a304d0093535fd6c0a001ae77611c020-d87f519f3535fbd50a001ae72ac1dc63-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "ERRor"
                    args = ["1", "OFF", "ON"]
                    
                class INFO(SCPINode, SCPIBool):
                    """
                    `SYSTem:ERRor:DISPlay:INFO
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/089aa3644bc14e4a.htm#ID_eb5520e93535ffdd0a001ae76a65fef0-e504a00a3535fe270a001ae72ac1dc63-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "INFO"
                    args = ["1", "OFF", "ON"]
                    
                class REMote(SCPINode, SCPIBool):
                    """
                    `SYSTem:ERRor:DISPlay:REMote
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/8bb7290d8cb44f14.htm#ID_b06832b2fab0c9c00a00206a00b9f04a-04495e7ffab0c4220a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "REMote"
                    args = ["1", "OFF", "ON"]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `SYSTem:ERRor:DISPlay:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/4531bcee03ac438e.htm#ID_da0c4734353604800a001ae72d74b408-99f5ef9e353603090a001ae72ac1dc63-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
                class WARNings(SCPINode, SCPIBool):
                    """
                    `SYSTem:ERRor:DISPlay:WARNings
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/089aa3644bc14e4a.htm#ID_d2602e9d353607010a001ae7089ac033-8bb3971d3536055b0a001ae72ac1dc63-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "WARNings"
                    args = ["1", "OFF", "ON"]
                    
            class NEXT(SCPINode, SCPIQuery):
                """
                `SYSTem:ERRor:NEXT
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e120908.htm#ID_7655f04ffab0d1510a00206a00680a86-25be5834fab0cbb40a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "NEXT"
                args = [""]
                
        class FIRMware(SCPINode):
            """
            SYSTem:FIRMware
            
            Arguments: 
            """
            _cmd = "FIRMware"
            args = [""]
            
            class UPDate(SCPINode, SCPISet):
                """
                `SYSTem:FIRMware:UPDate
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e120935.htm#ID_0bcb7667fab0d8d30a00206a00b6a20a-9fd656e1fab0d3360a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "UPDate"
                args = ["'string'"]
                
        class FPReset(SCPINode, SCPISet):
            """
            `SYSTem:FPReset
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e120967.htm#ID_f22e24cafab0e0650a00206a00d64c6a-b86b5b25fab0dab80a00206a01a6673d-en-US>`_
            
            Arguments: 
            """
            _cmd = "FPReset"
            args = [""]
            
        class FREQuency(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:FREQuency
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e120989.htm#ID_1a39d97dfab0e7f60a00206a018a7f6e-2fc01ddafab0e2390a00206a01a6673d-en-US>`_
            
            Arguments: MAXimum, MINimum
            """
            _cmd = "FREQuency"
            args = ["MAXimum", "MINimum"]
            
        class IDENtify(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:IDENtify
            
            Arguments: 'string'
            """
            _cmd = "IDENtify"
            args = ["'string'"]
            
            class FACTory(SCPINode, SCPISet):
                """
                `SYSTem:IDENtify:FACTory
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121040.htm#ID_c1695db591e160a10a00206a00cd77f5-e99d3c9c91e158440a00206a00e9ecac-en-US>`_
                
                Arguments: 
                """
                _cmd = "FACTory"
                args = [""]
                
            class STRing(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:IDENtify:STRing
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121068.htm#ID_437487be91e16d910a00206a003f7503-85833b1a91e164a80a00206a00e9ecac-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "STRing"
                args = ["'string'"]
                
        class INFO(SCPINode):
            """
            SYSTem:INFO
            
            Arguments: 
            """
            _cmd = "INFO"
            args = [""]
            
            class CONTrast(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:INFO:CONTrast
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e4e198e6eab14f2c.htm#ID_961fc2d6842f14130a00201900e72704-c596e387842f12ab0a00201901936165-en-US>`_
                
                Arguments: 1
                """
                _cmd = "CONTrast"
                args = ["1"]
                
        class KLOCk(SCPINode, SCPIBool):
            """
            `SYSTem:KLOCk
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121133.htm#ID_9346e83cfab0ef780a00206a01c95e16-25df267cfab0e9cb0a00206a01a6673d-en-US>`_
            
            Arguments: 1, OFF, ON
            """
            _cmd = "KLOCk"
            args = ["1", "OFF", "ON"]
            
        class LANGuage(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:LANGuage
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121162.htm#ID_869a87e0fab0f70a0a00206a0129131e-f2c4c937fab0f15c0a00206a01a6673d-en-US>`_
            
            Arguments: 'string'
            """
            _cmd = "LANGuage"
            args = ["'string'"]
            
        class LOGGing(SCPINode):
            """
            SYSTem:LOGGing
            
            Arguments: 
            """
            _cmd = "LOGGing"
            args = [""]
            
            class REMote(SCPINode, SCPIBool):
                """
                SYSTem:LOGGing:REMote
                
                Arguments: 1, OFF, ON
                """
                _cmd = "REMote"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `SYSTem:LOGGing:REMote:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121211.htm#ID_2859a837fab0feab0a00206a0104b6ad-22b5a74ffab0f8ee0a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
        class NOPeration(SCPINode, SCPISet):
            """
            SYSTem:NOPeration
            
            Arguments: 
            """
            _cmd = "NOPeration"
            args = [""]
            
        class OPTions(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:OPTions
            
            Arguments: 'string'
            """
            _cmd = "OPTions"
            args = ["'string'"]
            
            class DISable(SCPINode, SCPISet):
                """
                SYSTem:OPTions:DISable
                
                Arguments: 'string'
                """
                _cmd = "DISable"
                args = ["'string'"]
                
            class FACTory(SCPINode, SCPISet):
                """
                `SYSTem:OPTions:FACTory
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121251.htm#ID_efb9e44791e18d2f0a00206a01117c44-73da166c91e183f80a00206a00e9ecac-en-US>`_
                
                Arguments: 
                """
                _cmd = "FACTory"
                args = [""]
                
            class STRing(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:OPTions:STRing
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121276.htm#ID_fcf476dc91e1979f0a00206a008bad5a-3055959091e18fdf0a00206a00e9ecac-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "STRing"
                args = ["'string'"]
                
        class PASSword(SCPINode, SCPISet):
            """
            SYSTem:PASSword
            
            Arguments: 'string'
            """
            _cmd = "PASSword"
            args = ["'string'"]
            
            class CENable(SCPINode, SCPISet):
                """
                `SYSTem:PASSword:CENable
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121353.htm#ID_5deccfb4fab1062c0a00206a015e85f5-4817c3fbfab1008f0a00206a01a6673d-en-US>`_
                
                Arguments: 'string'
                """
                _cmd = "CENable"
                args = ["'string'"]
                
        class PRESet(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:PRESet
            
            Arguments: 
            """
            _cmd = "PRESet"
            args = [""]
            
            class DUMMy(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:PRESet:DUMMy
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121573.htm#ID_0ce589adfab124920a00206a01485f4a-3a5f7062fab11e960a00206a01a6673d-en-US>`_
                
                Arguments: 
                """
                _cmd = "DUMMy"
                args = [""]
                
            class REMote(SCPINode, SCPIBool):
                """
                SYSTem:PRESet:REMote
                
                Arguments: 1, OFF, ON
                """
                _cmd = "REMote"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `SYSTem:PRESet:REMote:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9fcef3bb614f452b.htm#ID_9e274d9e581341e70a001ae771e5dcc6-f3df5f90581340700a001ae75f9ff217-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class SCOPe(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:PRESet:SCOPe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121385.htm#ID_f14f0f4efab10d9f0a00206a00724e94-7cbf2c2dfab108110a00206a01a6673d-en-US>`_
                
                Arguments: ALL, SINGle
                """
                _cmd = "SCOPe"
                args = ["ALL", "SINGle"]
                
            class USER(SCPINode, SCPIBool):
                """
                SYSTem:PRESet:USER
                
                Arguments: 1, OFF, ON
                """
                _cmd = "USER"
                args = ["1", "OFF", "ON"]
                
                class CAL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:PRESet:USER:CAL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/f0cd6bd78b8a463c.htm#ID_929a0b5bac61eaa90a00201900cbe46b-37784b03ac61e99f0a0020190003471b-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "CAL"
                    args = ["'string'"]
                    
                class NAME(SCPINode, SCPIQuery, SCPISet):
                    """
                    `SYSTem:PRESet:USER:NAME
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121429.htm#ID_9e06eeaefab115300a00206a00cb4ce5-0538d3bbfab10f830a00206a01a6673d-en-US>`_
                    
                    Arguments: 'string'
                    """
                    _cmd = "NAME"
                    args = ["'string'"]
                    
                class STATe(SCPINode, SCPIBool):
                    """
                    `SYSTem:PRESet:USER:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121465.htm#ID_66b8f316fab11cc20a00206a0087213c-35caa738fab117050a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
        class PRIority(SCPINode, SCPIQuery, SCPISet):
            """
            SYSTem:PRIority
            
            Arguments: ANORmal, HIGH, NORMal
            """
            _cmd = "PRIority"
            args = ["ANORmal", "HIGH", "NORMal"]
            
        class SETTings(SCPINode):
            """
            SYSTem:SETTings
            
            Arguments: 
            """
            _cmd = "SETTings"
            args = [""]
            
            class UPDate(SCPINode, SCPISet):
                """
                `SYSTem:SETTings:UPDate
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121631.htm#ID_e5afdc76fab134220a00206a00902fa2-2837511dfab12e360a00206a01a6673d-en-US>`_
                
                Arguments: ONCE
                """
                _cmd = "UPDate"
                args = ["ONCE"]
                
        class SHUTdown(SCPINode, SCPISet):
            """
            `SYSTem:SHUTdown
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/def2e5e153454147.htm#ID_19d5020713577b1b0a00206a019388f2-1efe305b1357755e0a00206a0182dc26-en-US>`_
            
            Arguments: ABORt, CLOSe, HALT, REBoot, RESTart
            """
            _cmd = "SHUTdown"
            args = ["ABORt", "CLOSe", "HALT", "REBoot", "RESTart"]
            
        class SMATrix(SCPINode):
            """
            SYSTem:SMATrix
            
            Arguments: 
            """
            _cmd = "SMATrix"
            args = [""]
            
            class OPTimization(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:SMATrix:OPTimization
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/6c0a61c173ee4de7.htm#ID_5e9bd4c9e2b551800a0020190004db0c-b8f06f0be2b550470a002019017b841c-en-US>`_
                
                Arguments: PRECision, SPEed
                """
                _cmd = "OPTimization"
                args = ["PRECision", "SPEed"]
                
        class SOUNd(SCPINode):
            """
            SYSTem:SOUNd
            
            Arguments: 
            """
            _cmd = "SOUNd"
            args = [""]
            
            class ALARm(SCPINode, SCPIBool):
                """
                SYSTem:SOUNd:ALARm
                
                Arguments: 1, OFF, ON
                """
                _cmd = "ALARm"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `SYSTem:SOUNd:ALARm:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2a6409afa1604928.htm#ID_cf6e6360fab13bf20a00206a01a85018-52ea9190fab136060a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
            class STATus(SCPINode, SCPIBool):
                """
                SYSTem:SOUNd:STATus
                
                Arguments: 1, OFF, ON
                """
                _cmd = "STATus"
                args = ["1", "OFF", "ON"]
                
                class STATe(SCPINode, SCPIBool):
                    """
                    `SYSTem:SOUNd:STATus:STATe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2a6409afa1604928.htm#ID_a23de053fab143740a00206a00e3a371-80e149c4fab13dd60a00206a01a6673d-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "STATe"
                    args = ["1", "OFF", "ON"]
                    
        class TIME(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:TIME
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/a7965f84d8ac4a09.htm#ID_c96fbd06aaa8f6690a00206a01148777-6b4f287aaaa8ea530a00206a00dee6b8-en-US>`_
            
            Arguments: 1
            """
            _cmd = "TIME"
            args = ["1"]
            
            class INTermediate(SCPINode, SCPIQuery):
                """
                SYSTem:TIME:INTermediate
                
                Arguments: 
                """
                _cmd = "INTermediate"
                args = [""]
                
            class STARt(SCPINode, SCPISet):
                """
                SYSTem:TIME:STARt
                
                Arguments: 
                """
                _cmd = "STARt"
                args = [""]
                
            class STOP(SCPINode, SCPIQuery):
                """
                SYSTem:TIME:STOP
                
                Arguments: 
                """
                _cmd = "STOP"
                args = [""]
                
            class SYNC(SCPINode, SCPISet):
                """
                SYSTem:TIME:SYNC
                
                Arguments: 
                """
                _cmd = "SYNC"
                args = [""]
                
        class TSLock(SCPINode, SCPIQuery, SCPISet):
            """
            `SYSTem:TSLock
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121846.htm#ID_48769b733516bd2c0a00206a005ec64c-a13ed1c43516b4a10a00206a01f2dc17-en-US>`_
            
            Arguments: DIAGrams, OFF, SCReen
            """
            _cmd = "TSLock"
            args = ["DIAGrams", "OFF", "SCReen"]
            
        class USER(SCPINode):
            """
            SYSTem:USER
            
            Arguments: 
            """
            _cmd = "USER"
            args = [""]
            
            class DISPlay(SCPINode):
                """
                SYSTem:USER:DISPlay
                
                Arguments: 
                """
                _cmd = "DISPlay"
                args = [""]
                
                class TITLe(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:USER:DISPlay:TITLe
                    
                    Arguments: 'string'
                    """
                    _cmd = "TITLe"
                    args = ["'string'"]
                    
            class FKEY(SCPINode, SCPIQuery, SCPISet):
                """
                SYSTem:USER:FKEY
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "FKEY"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class KEY(SCPINode, SCPIQuery, SCPISet):
                """
                `SYSTem:USER:KEY
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e121896.htm#ID_5b19f768fab15a190a00206a003ab4cd-5c1d14c8fab1547b0a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "KEY"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
                class FUNCtion(SCPINode, SCPIQuery, SCPISet):
                    """
                    SYSTem:USER:KEY:FUNCtion
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "FUNCtion"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
        class VERSion(SCPINode, SCPIQuery):
            """
            `SYSTem:VERSion
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/695c6313296c4a8a.htm#ID_ae289010fab1693c0a00206a008797a2-0d4d3fbffab1637f0a00206a01a6673d-en-US>`_
            
            Arguments: 
            """
            _cmd = "VERSion"
            args = [""]
            
        class WAIT(SCPINode, SCPISet):
            """
            SYSTem:WAIT
            
            Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
            """
            _cmd = "WAIT"
            args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
            
    class TRACe(SCPINode, SCPIQuery, SCPISet):
        """
        TRACe
        
        Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
        """
        _cmd = "TRACe"
        args = ["CH1Data", "CH1Mem", "CH2Data", "CH2Mem", "CH3Data", "CH3Mem", "CH4Data", "CH4Mem", "MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8"]
        
        class CLEar(SCPINode, SCPISet):
            """
            `TRACe:CLEar
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ac86031e502949ce.htm#ID_64dd94bdfab178ad0a00206a007cb1e5-5b0e530efab1730f0a00206a01a6673d-en-US>`_
            
            Arguments: MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
            """
            _cmd = "CLEar"
            args = ["MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8"]
            
        class COPY(SCPINode, SCPISet):
            """
            `TRACe:COPY
            <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e122210.htm#ID_701570b0fab1805d0a00206a00ce1355-b06fb49ffab17aa10a00206a01a6673d-en-US>`_
            
            Arguments: MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8, 'string'
            """
            _cmd = "COPY"
            args = ["MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8", "'string'"]
            
            class MATH(SCPINode, SCPISet):
                """
                `TRACe:COPY:MATH
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e122305.htm#ID_8db7b1cffab1880e0a00206a015a07f4-f95d19b4fab182510a00206a01a6673d-en-US>`_
                
                Arguments: MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8, 'string'
                """
                _cmd = "MATH"
                args = ["MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8", "'string'"]
                
        class DATA(SCPINode, SCPIQuery, SCPISet):
            """
            TRACe:DATA
            
            Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
            """
            _cmd = "DATA"
            args = ["CH1Data", "CH1Mem", "CH2Data", "CH2Mem", "CH3Data", "CH3Mem", "CH4Data", "CH4Mem", "MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8"]
            
            class RESPonse(SCPINode, SCPIQuery, SCPISet):
                """
                TRACe:DATA:RESPonse
                
                Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
                """
                _cmd = "RESPonse"
                args = ["CH1Data", "CH1Mem", "CH2Data", "CH2Mem", "CH3Data", "CH3Mem", "CH4Data", "CH4Mem", "MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8"]
                
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRACe:DATA:RESPonse:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e125848.htm#ID_2a0bba9afab1979e0a00206a01b06d03-c178a5b4fab191c20a00206a01a6673d-en-US>`_
                    
                    Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
                    """
                    _cmd = "ALL"
                    args = ["CH1Data", "CH1Mem", "CH2Data", "CH2Mem", "CH3Data", "CH3Mem", "CH4Data", "CH4Mem", "MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8"]
                    
            class STIMulus(SCPINode, SCPIQuery, SCPISet):
                """
                TRACe:DATA:STIMulus
                
                Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
                """
                _cmd = "STIMulus"
                args = ["CH1Data", "CH1Mem", "CH2Data", "CH2Mem", "CH3Data", "CH3Mem", "CH4Data", "CH4Mem", "MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8"]
                
                class ALL(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRACe:DATA:STIMulus:ALL
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d36e125921.htm#ID_b73c7a35fab18fde0a00206a00c988a1-92a8d8b0fab189f20a00206a01a6673d-en-US>`_
                    
                    Arguments: CH1Data, CH1Mem, CH2Data, CH2Mem, CH3Data, CH3Mem, CH4Data, CH4Mem, MDATa1, MDATa2, MDATa3, MDATa4, MDATa5, MDATa6, MDATa7, MDATa8
                    """
                    _cmd = "ALL"
                    args = ["CH1Data", "CH1Mem", "CH2Data", "CH2Mem", "CH3Data", "CH3Mem", "CH4Data", "CH4Mem", "MDATa1", "MDATa2", "MDATa3", "MDATa4", "MDATa5", "MDATa6", "MDATa7", "MDATa8"]
                    
    class TRIGger(SCPINodeN):
        """
        TRIGger
        
        Arguments: 
        """
        _cmd = "TRIGger"
        args = [""]
        
        class CHANnel(SCPINodeN):
            """
            TRIGger:CHANnel
            
            Arguments: 
            """
            _cmd = "CHANnel"
            args = [""]
            
            class AUXiliary(SCPINodeN, SCPIBool):
                """
                TRIGger:CHANnel:AUXiliary
                
                Arguments: 1, OFF, ON
                """
                _cmd = "AUXiliary"
                args = ["1", "OFF", "ON"]
                
                class DURation(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:CHANnel:AUXiliary:DURation
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2ec0bc6b13f2415c.htm#ID_862e541aaaa940c00a00206a00c23306-85574235aaa935e20a00206a00dee6b8-en-US>`_
                    
                    Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                    """
                    _cmd = "DURation"
                    args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                    
                class ENABle(SCPINode, SCPIBool):
                    """
                    `TRIGger:CHANnel:AUXiliary:ENABle
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/2f050fb4094d4096.htm#ID_47359972aaa9507f0a00206a00d85789-5734e0b5aaa943dc0a00206a00dee6b8-en-US>`_
                    
                    Arguments: 1, OFF, ON
                    """
                    _cmd = "ENABle"
                    args = ["1", "OFF", "ON"]
                    
                class INTerval(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:CHANnel:AUXiliary:INTerval
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/fb7f8a046d20447a.htm#ID_6e115f17aaa95ddd0a00206a00669cd7-e8362417aaa952b10a00206a00dee6b8-en-US>`_
                    
                    Arguments: POINt, SWEep
                    """
                    _cmd = "INTerval"
                    args = ["POINt", "SWEep"]
                    
                class OPOLarity(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:CHANnel:AUXiliary:OPOLarity
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/d4cfc80a1c194fc3.htm#ID_a10e8d4caaa96bc70a00206a01c30908-19056cd3aaa9605d0a00206a00dee6b8-en-US>`_
                    
                    Arguments: NEGative, POSitive
                    """
                    _cmd = "OPOLarity"
                    args = ["NEGative", "POSitive"]
                    
                class POSition(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:CHANnel:AUXiliary:POSition
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ddbb6ff54bfa4e49.htm#ID_0e644885aaa979540a00206a0189b3a3-f58ab43aaaa96e480a00206a00dee6b8-en-US>`_
                    
                    Arguments: AFTer, BEFore
                    """
                    _cmd = "POSition"
                    args = ["AFTer", "BEFore"]
                    
        class SEQuence(SCPINode):
            """
            TRIGger:SEQuence
            
            Arguments: 
            """
            _cmd = "SEQuence"
            args = [""]
            
            class HOLDoff(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:HOLDoff
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/c7a1eba08bbc44bb.htm#ID_b0e57a38fab19f200a00206a00cbaf37-80f2d0b6fab199730a00206a01a6673d-en-US>`_
                
                Arguments: 1, DEFault, DOWN, MAXimum, MINimum, UP
                """
                _cmd = "HOLDoff"
                args = ["1", "DEFault", "DOWN", "MAXimum", "MINimum", "UP"]
                
            class LINK(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:LINK
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/e09399d307a34f01.htm#ID_a4da22c4fab1a6c10a00206a01179287-42cdd25ffab1a1050a00206a01a6673d-en-US>`_
                
                Arguments: 'POINt', 'PPOint', 'SEGMent', 'SWEep'
                """
                _cmd = "LINK"
                args = ["'POINt'", "'PPOint'", "'SEGMent'", "'SWEep'"]
                
            class MULTiple(SCPINode):
                """
                TRIGger:SEQuence:MULTiple
                
                Arguments: 
                """
                _cmd = "MULTiple"
                args = [""]
                
                class HOLDoff(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:SEQuence:MULTiple:HOLDoff
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/020b4a1c90f348ff.htm#ID_adddb58013579dc60a00206a0121e541-a514b3ce135797fa0a00206a0182dc26-en-US>`_
                    
                    Arguments: POINt, PPOint, SEGMent, SWEep
                    """
                    _cmd = "HOLDoff"
                    args = ["POINt", "PPOint", "SEGMent", "SWEep"]
                    
                class SLOPe(SCPINodeN, SCPIQuery, SCPISet):
                    """
                    `TRIGger:SEQuence:MULTiple:SLOPe
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/ff1d260400c24bdf.htm#ID_af1475ce1357a5a60a00206a01d52097-fc26c60f13579fca0a00206a0182dc26-en-US>`_
                    
                    Arguments: POINt, PPOint, SEGMent, SWEep
                    """
                    _cmd = "SLOPe"
                    args = ["POINt", "PPOint", "SEGMent", "SWEep"]
                    
                class SOURce(SCPINode, SCPIQuery, SCPISet):
                    """
                    `TRIGger:SEQuence:MULTiple:SOURce
                    <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/12f6a33395644026.htm#ID_f37037d61357ad760a00206a00a7072a-cf0a0a421357a7a90a00206a0182dc26-en-US>`_
                    
                    Arguments: POINt, PPOint, SEGMent, SWEep
                    """
                    _cmd = "SOURce"
                    args = ["POINt", "PPOint", "SEGMent", "SWEep"]
                    
            class SLOPe(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:SLOPe
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/cbc5449b57664ad3.htm#ID_cb1b57a0fab1d4f50a00206a0000a5cb-21b2e7d1fab1cf580a00206a01a6673d-en-US>`_
                
                Arguments: HIGH, LOW, NEGative, POSitive
                """
                _cmd = "SLOPe"
                args = ["HIGH", "LOW", "NEGative", "POSitive"]
                
            class SOURce(SCPINode, SCPIQuery, SCPISet):
                """
                `TRIGger:SEQuence:SOURce
                <http://www.rohde-schwarz.com/webhelp/znb_znbt_webhelp_en_7/Content/9c62999c5a1642f2.htm#ID_3ee3f346fab1dc770a00206a0037b055-0940f367fab1d6da0a00206a01a6673d-en-US>`_
                
                Arguments: EXTernal, IMMediate, MANual, MULTiple
                """
                _cmd = "SOURce"
                args = ["EXTernal", "IMMediate", "MANual", "MULTiple"]
                
    # END OF ZNB_gen
