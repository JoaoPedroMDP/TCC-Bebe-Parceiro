import Swal from 'sweetalert2';


export class SwalFacade {

  /**
   * @description Representa um SweetAlert para informação de erro
   * 
   * @param titulo Obrigatório informar um titulo para o popup
   * @param texto Opcional, um texto extra de ajuda
   * 
   */
  static error(titulo: string, texto?: string): Promise<any> {
    const Toast = Swal.mixin({
      toast: true,
      position: 'top',
      showConfirmButton: false,
      timer: 2500,
      background: '#BA1414',
      color: '#ffffff',
      iconColor: '#ffffff',
      timerProgressBar: true,
      didOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer)
        toast.addEventListener('mouseleave', Swal.resumeTimer)
      }
    })

    return Toast.fire({
      icon: 'error',
      title: titulo,
      text: texto,
      confirmButtonColor: '#FFA516',
      confirmButtonText: 'Ok'
    })
  }

  /**
   * @description Representa um SweetAlert para informação de sucesso
   * 
   * @param titulo Obrigatório informar um titulo para o popup
   * @param texto Opcional, um texto extra de ajuda
   * 
   */
  static success(titulo: string, texto?: string): Promise<any> {
    const Toast = Swal.mixin({
      toast: true,
      position: 'top',
      showConfirmButton: false,
      timer: 1000,
      background: '#00ac00',
      color: '#ffffff',
      iconColor: '#ffffff',
      timerProgressBar: true,
      didOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer)
        toast.addEventListener('mouseleave', Swal.resumeTimer)
      }
    })

    return Toast.fire({
      icon: 'success',
      title: titulo,
      text: texto
    })
  }

  /**
   * @description Representa um SweetAlert para informação de alerta
   * 
   * @param titulo Obrigatório informar um titulo para o popup
   * @param texto Opcional, um texto extra de ajuda
   * 
   */
  static alert(titulo: string, texto?: string): Promise<any> {
    const Toast = Swal.mixin({
      toast: true,
      position: 'top',
      showConfirmButton: false,
      timer: 2500,
      background: '#FF5F1F',
      color: '#ffffff',
      iconColor: '#ffffff',
      timerProgressBar: true,
      didOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer)
        toast.addEventListener('mouseleave', Swal.resumeTimer)
      }
    })

    return Toast.fire({
      icon: 'warning',
      title: titulo,
      text: texto
    })
  }

}